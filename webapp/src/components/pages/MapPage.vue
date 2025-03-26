<template>
  <div
    v-if="isLoadingData"
    class="flex h-full w-full items-center justify-center"
  >
    <LoadingWheel />
  </div>
  <div v-else class="grid h-full w-full grid-cols-4 items-start justify-start">
    <div class="col-span-3 flex w-full flex-col items-start justify-start">
      <Europe class="w-full" />
      <div class="px-4 text-xs font-normal text-gray-500">
        Mode de Comparaison :
        <span v-if="comparison">On</span>
        <span v-else>Off</span>
      </div>
    </div>
    <div class="h-full w-full overflow-scroll">
      <div
        v-if="!selectedCountry.length"
        class="mx-auto max-w-80 items-center justify-center px-2 pt-10"
      >
        <div v-if="!comparison" class="min-h-56 text-lg text-ocean">
          <span class="font-semibold">Sélectionnez un pays </span>
          <span class="font-normal"
            >pour explorer en détail ses métriques de qualité de l'eau.</span
          >
        </div>
        <div v-else class="min-h-56 text-lg text-ocean">
          <span class="font-semibold">Sélectionnez deux pays </span>
          <span class="font-normal"
            >pour explorer en détail leurs métriques de qualité de l'eau et les
            comparer.</span
          >
        </div>
        <div class="flex flex-col gap-4 pr-4 text-sm">
          <div class="flex w-full flex-row items-end justify-start gap-5">
            <div>
              Envie de <span class="font-semibold">comparer</span> deux pays?
            </div>
            <Switch
              v-model="comparison"
              :class="comparison ? 'bg-ocean' : 'bg-gray-300'"
              class="relative inline-flex h-[18px] w-[34px] shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-white/75"
            >
              <span
                :class="comparison ? 'translate-x-4' : 'translate-x-0'"
                aria-hidden="true"
                class="pointer-events-none inline-block h-[14px] w-[14px] transform rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out"
              />
            </Switch>
          </div>
          <div>
            Activez le mode de comparaison avec le bouton ci-dessus, puis
            cliquez sur deux pays pour afficher les données de qualité de l'eau
            côte à côte.
          </div>
        </div>
      </div>
      <div
        v-if="
          selectedCountry.length &&
          generalInfo &&
          Object.keys(generalInfo).length > 0
        "
        class="w-full"
      >
        <MapTable
          :selected-country="selectedCountry"
          :general-info="generalInfo"
        />
      </div>
    </div>
  </div>

  <TransitionRoot :show="showPopUp" appear as="template">
    <ErrorPopUp
      title="Erreur de sélection"
      message="Vous ne pouvez sélectionner que deux pays à la fois pour
                  la comparaison. Veuillez désélectionner tous les pays ou un seul
                  pour en choisir un nouveau."
      left-label="Tout désélectionner"
      right-label="Laissez-moi choisir"
      :left-action="resetComparison"
      :right-action="togglePopUp"
    />
  </TransitionRoot>
</template>

<script lang="ts" setup>
import Europe from "@/components/pages/EuropeMap.vue"
import { computed, onMounted, ref } from "vue"
import { Switch, TransitionRoot } from "@headlessui/vue"
import type * as types from "@/type"
import LoadingWheel from "@/components/share/LoadingWheel.vue"
import ErrorPopUp from "@/components/reusable/popups/ErrorPopUp.vue"
import MapTable from "@/components/tables/MapTable.vue"
import axios from "axios"

const isLoadingData = computed(() => {
  return availableCountries.value.length === 0
})
const selectedCountry = ref<types.Country[]>([])
const availableCountries = ref<types.Country[]>([])
const generalInfo = ref<{ [key: string]: types.CountryGeneralInfo }>({})

const fetchData = async () => {
  try {
    const response = await axios.get("/api/data/map/list-countries/")
    availableCountries.value = response.data
  } catch (error) {
    console.error(error)
  }
}

const setupMap = async () => {
  const paths = document.querySelectorAll("#countries path")

  if (paths.length > 0) {
    paths.forEach((path) => {
      const isoAlpha2 = path.getAttribute("id")?.toString().toUpperCase()
      const isAvailable = availableCountries.value.some(
        (country) => country.code === isoAlpha2
      )

      if (isAvailable) {
        path.classList.add(
          "fill-gray-200",
          "stroke-gray-600",
          "transition-all",
          "duration-200",
          "ease-in-out",
          "hover:fill-ocean",
          "hover:cursor-pointer"
        )

        path.addEventListener("click", async function () {
          const country = availableCountries.value.find(
            (country) => country.code === isoAlpha2
          )

          if (country) {
            if (country.clicked) {
              path.classList.remove("fill-ocean")
              path.classList.add("fill-gray-200")
              country.clicked = false
              selectedCountry.value.splice(
                selectedCountry.value.indexOf(country),
                1
              )
              delete generalInfo.value[country.code]
            } else if (comparison.value) {
              const numberClicked = availableCountries.value.filter(
                (s) => s.clicked
              ).length
              if (numberClicked == 2) {
                console.error("You can't select more than 2 countries")
                showPopUp.value = true
              } else {
                path.classList.remove("fill-gray-200")
                path.classList.add("fill-ocean")
                country.clicked = true
                selectedCountry.value.push(country)
                try {
                  const response = await axios.get(
                    `/api/data/map/general-info?country_code=${country.code}`
                  )
                  generalInfo.value[country.code] = response.data
                } catch (error) {
                  console.error(error)
                }
              }
            } else {
              availableCountries.value.forEach((otherCountry) => {
                if (otherCountry.clicked) {
                  const otherPath = document.getElementById(
                    `${otherCountry.code.toLowerCase()}`
                  )
                  if (otherPath) {
                    otherPath.classList.remove("fill-ocean")
                    otherPath.classList.add("fill-gray-200")
                    otherCountry.clicked = false
                    selectedCountry.value.splice(
                      selectedCountry.value.indexOf(country),
                      1
                    )
                    delete generalInfo.value[country.code]
                  }
                }
                path.classList.remove("fill-gray-200")
                path.classList.add("fill-ocean")
                country.clicked = true
              })

              selectedCountry.value.push(country)
              try {
                const response = await axios.get(
                  `/api/data/map/general-info?country_code=${country.code}`
                )
                generalInfo.value[country.code] = response.data
              } catch (error) {
                console.error(error)
              }
            }
          }
        })
      } else {
        path.classList.add("fill-gray-400", "stroke-gray-600")
      }
    })
  } else {
    console.error("No paths found inside #countries")
  }
}

onMounted(async () => {
  await fetchData()
  await setupMap()
})
const comparison = ref(false)
const showPopUp = ref(false)

const resetComparison = () => {
  const selectedAll = availableCountries.value.filter(function (s) {
    return s.clicked
  })
  selectedAll.forEach((country) => {
    const otherPath = document.getElementById(`${country.code.toLowerCase()}`)
    if (otherPath) {
      otherPath.classList.remove("fill-ocean")
      otherPath.classList.add("fill-gray-200")
      country.clicked = false
      selectedCountry.value.splice(selectedCountry.value.indexOf(country), 1)
      delete generalInfo.value[country.code]
    }
  })
  togglePopUp()
}

const togglePopUp = () => {
  showPopUp.value = !showPopUp.value
}
</script>
