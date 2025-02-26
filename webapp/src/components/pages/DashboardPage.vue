<template>
  <div
    class="flex h-full w-full flex-col items-start justify-between p-12 py-4 gap-2"
  >
    <div class="flex flex-row gap-3">
      <SelectOption
        :default="
          countries.find((country) => country.name === route.query.country) ||
          countries[0]
        "
        :label="'Country'"
        :rowData="countries"
      />
      <SelectOption
        :default="decades[0]"
        :label="'Decades'"
        :rowData="decades"
      />
      <SelectOption
        :default="chemicals[0]"
        :label="'Chemicals'"
        :rowData="chemicals"
      />
    </div>
    <div class="flex w-full flex-row items-center justify-between gap-2">
      <div
        class="h-fit min-h-24 w-56 rounded-lg bg-aqua/25 p-3 px-4 text-ocean shadow-lg"
      >
        <div class="flex flex-col items-start gap-8">
          <div class="flex w-full flex-row items-center justify-between">
            <Chemicals class="h-10 w-10 rounded-lg bg-aqua/35 fill-ocean p-2" />
            <div class="pr-6 text-2xl font-bold">6</div>
          </div>
          <div class="flex w-full flex-row items-center justify-between">
            <div class="text-xs font-normal">Count of Chemicals Monitored</div>
            <div class="group relative">
              <InformationCircleIcon
                class="h-4 w-4 cursor-pointer text-ocean"
              />

              <!-- Tooltip -->
              <div
                class="translate-x-1/5 absolute right-0 top-6 z-10 hidden w-fit min-w-32 max-w-56 rounded-md bg-ocean px-2 py-1 text-center text-[0.7rem] text-white opacity-0 shadow-md transition-opacity duration-200 group-hover:block group-hover:opacity-100"
              >
                More info about chemicals monitored
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        class="h-fit min-h-24 w-56 rounded-lg bg-aqua/25 p-3 px-4 text-ocean shadow-lg"
      >
        <div class="flex flex-col items-start gap-8">
          <div class="flex w-full flex-row items-center justify-between">
            <WebDomain class="h-10 w-10 rounded-lg bg-aqua/35 fill-ocean p-2" />
            <div class="pr-6 text-2xl font-bold">2</div>
          </div>
          <div class="flex w-full flex-row items-center justify-between">
            <div class="text-xs font-normal">Count of Monitoring Sites</div>
            <div class="group relative">
              <InformationCircleIcon
                class="h-4 w-4 cursor-pointer text-ocean"
              />

              <!-- Tooltip -->
              <div
                class="translate-x-1/5 absolute right-0 top-6 z-10 hidden w-fit min-w-32 max-w-56 rounded-md bg-ocean px-2 py-1 text-center text-[0.7rem] text-white opacity-0 shadow-md transition-opacity duration-200 group-hover:block group-hover:opacity-100"
              >
                More info about monitoring sites
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        class="h-fit min-h-24 w-56 rounded-lg bg-aqua/25 p-3 px-4 text-ocean shadow-lg"
      >
        <div class="flex flex-col items-start gap-8">
          <div class="flex w-full flex-row items-center justify-between">
            <Sample class="h-10 w-10 rounded-lg bg-aqua/35 fill-ocean p-2" />
            <div class="pr-6 text-2xl font-bold">256</div>
          </div>
          <div class="flex w-full flex-row items-center justify-between">
            <div class="text-xs font-normal">Number of Collected Samples</div>
            <div class="group relative">
              <InformationCircleIcon
                class="h-4 w-4 cursor-pointer text-ocean"
              />

              <!-- Tooltip -->
              <div
                class="translate-x-1/5 absolute right-0 top-6 z-10 hidden w-fit min-w-32 max-w-56 rounded-md bg-ocean px-2 py-1 text-center text-[0.7rem] text-white opacity-0 shadow-md transition-opacity duration-200 group-hover:block group-hover:opacity-100"
              >
                More info about collected samples
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        class="h-fit min-h-24 w-56 rounded-lg bg-aqua/25 p-3 px-4 text-ocean shadow-lg"
      >
        <div class="flex flex-col items-start gap-8">
          <div class="flex w-full flex-row items-center justify-between">
            <Proportion
              class="h-10 w-10 rounded-lg bg-aqua/35 fill-ocean p-2"
            />
            <div class="pr-6 text-2xl font-bold">
              2<span class="pl-1 text-xs">%</span>
            </div>
          </div>
          <div class="flex w-full flex-row items-center justify-between">
            <div class="text-left text-xs font-normal">
              Proportion Of Confirmed Samples
            </div>
            <div class="group relative">
              <InformationCircleIcon
                class="h-4 w-4 cursor-pointer text-ocean"
              />

              <!-- Tooltip -->
              <div
                class="translate-x-1/5 absolute right-0 top-6 z-10 hidden w-fit min-w-32 max-w-56 rounded-md bg-ocean px-2 py-1 text-center text-[0.7rem] text-white opacity-0 shadow-md transition-opacity duration-200 group-hover:block group-hover:opacity-100"
              >
                More info about confirmed samples
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="flex w-full flex-row items-center gap-8">
      <div class="h-full min-h-fit w-full rounded-lg bg-white p-2 py-3 shadow">
        <div class="flex w-full flex-row items-center gap-4 px-3 py-2 pt-0">
          <div class="text-sm font-semibold text-ocean">
            Overview of Chemical Measurements Across Sites
          </div>
          <div class="group relative">
            <InformationCircleIcon class="h-4 w-4 cursor-pointer text-ocean" />
            <!-- Tooltip -->
            <div
              class="translate-x-1/5 absolute right-0 top-6 z-10 hidden w-fit min-w-32 max-w-56 rounded-md bg-black/80 px-2 py-1 text-center text-[0.7rem] text-white opacity-0 shadow-md transition-opacity duration-200 group-hover:block group-hover:opacity-100"
            >
              More info about missing data.
            </div>
          </div>
        </div>

        <div class="h-36 overflow-y-auto">
          <table class="min-w-full">
            <thead>
              <tr class="border-b border-gray-200 text-center text-xs">
                <th class="px-4 py-2">Chemical</th>
                <th class="px-4 py-2">Count</th>
                <th class="px-4 py-2">Mean</th>
                <th class="px-4 py-2">Min</th>
                <th class="px-4 py-2">Max</th>
                <th class="px-4 py-2">Std Dev</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(chemical, index) in paginatedChemicals"
                :key="index"
                class="text-center text-xs"
              >
                <td class="w-56 px-4 py-2">{{ chemical.name }}</td>
                <td class="px-4 py-2">{{ chemical.count }}</td>
                <td class="px-4 py-2">{{ chemical.mean }}</td>
                <td class="px-4 py-2">{{ chemical.min }}</td>
                <td class="px-4 py-2">{{ chemical.max }}</td>
                <td class="px-4 py-2">{{ chemical.stdDev }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- Pagination -->
        <div
          v-if="totalPages > 1"
          class="flex items-center justify-center gap-4"
        >
          <div
            :disabled="currentPage === 1"
            class="text-ocen text-xs font-semibold"
            @click="prevPage"
          >
            <ChevronLeftIcon
              class="h-4 w-4 text-gray-500 hover:cursor-pointer hover:text-ocean"
            />
          </div>
          <div class="text-xs">Page {{ currentPage }} of {{ totalPages }}</div>
          <div
            :disabled="currentPage === totalPages"
            class="text-ocen text-xs font-semibold"
            @click="nextPage"
          >
            <ChevronRightIcon
              class="h-4 w-4 text-gray-500 hover:cursor-pointer hover:text-ocean"
            />
          </div>
        </div>
      </div>
      <div class="-ml-24 h-40 w-fit">
        <DonutChart :chartData="data" />
      </div>
    </div>
    <div class="flex w-full flex-row items-center justify-between gap-8">
      <div class="h-fit min-h-64 w-1/2 rounded-lg bg-white p-3 px-6 shadow">
        <div class="flex w-full flex-row items-center gap-4 px-3 py-2 pt-0">
          <div class="text-sm font-semibold text-ocean">
            Average Observed Values Over Time
          </div>
          <div class="group relative">
            <InformationCircleIcon class="h-4 w-4 cursor-pointer text-ocean" />

            <!-- Tooltip -->
            <div
              class="translate-x-1/5 absolute right-0 top-6 z-10 hidden w-fit min-w-32 max-w-56 rounded-md bg-ocean px-2 py-1 text-center text-[0.7rem] text-white opacity-0 shadow-md transition-opacity duration-200 group-hover:block group-hover:opacity-100"
            >
              More info about missing data.
            </div>
          </div>
        </div>
        <LineChart :chartData="data" />
      </div>
      <div class="h-fit min-h-64 w-1/2 rounded-lg bg-white p-3 px-6 shadow">
        <div class="flex w-full flex-row items-center gap-4 px-3 py-2 pt-0">
          <div class="text-sm font-semibold text-ocean">
            Most Monitored Determinands
          </div>
          <div class="group relative">
            <InformationCircleIcon class="h-4 w-4 cursor-pointer text-ocean" />

            <!-- Tooltip -->
            <div
              class="translate-x-1/5 absolute right-0 top-6 z-10 hidden w-fit min-w-32 max-w-56 rounded-md bg-ocean px-2 py-1 text-center text-[0.7rem] text-white opacity-0 shadow-md transition-opacity duration-200 group-hover:block group-hover:opacity-100"
            >
              More info about missing data.
            </div>
          </div>
        </div>
        <BarChart :chartData="data" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { computed, ref } from "vue"
import { useRoute } from "vue-router"
import {
  ChevronLeftIcon,
  ChevronRightIcon,
  InformationCircleIcon,
} from "@heroicons/vue/24/outline"
import type * as types from "@/type"
import SelectOption from "@/components/reusable/dropdowns/SelectOption.vue"
import BarChart from "@/components/reusable/charts/BarChart.vue"
import DonutChart from "@/components/reusable/charts/DonutChart.vue"
import LineChart from "@/components/reusable/charts/LineChart.vue"
import Chemicals from "@/assets/icons/Chemicals.vue"
import WebDomain from "@/assets/icons/WebDomain.vue"
import Sample from "@/assets/icons/Sample.vue"
import Proportion from "@/assets/icons/Proportion.vue"

const route = useRoute()

const allChemicals = ref([
  {
    name: "Trichloromethane",
    mean: 0.01,
    min: 0.01,
    max: 0.02,
    stdDev: 0.005,
    count: 6,
  },
  {
    name: "Fenthion",
    mean: 0.02,
    min: 0.01,
    max: 0.03,
    stdDev: 0.007,
    count: 4,
  },
  {
    name: "Chloridazon",
    mean: 0.015,
    min: 0.01,
    max: 0.02,
    stdDev: 0.006,
    count: 1,
  },
  {
    name: "Thallium",
    mean: 0.05,
    min: 0.04,
    max: 0.06,
    stdDev: 0.008,
    count: 9,
  },
  {
    name: "Aldicarb",
    mean: 0.03,
    min: 0.02,
    max: 0.04,
    stdDev: 0.009,
    count: 7,
  },
  {
    name: "Malathion",
    mean: 0.04,
    min: 0.02,
    max: 0.05,
    stdDev: 0.01,
    count: 5,
  },
  {
    name: "Atrazine",
    mean: 0.05,
    min: 0.04,
    max: 0.07,
    stdDev: 0.02,
    count: 8,
  },
  {
    name: "Glyphosate",
    mean: 0.02,
    min: 0.01,
    max: 0.03,
    stdDev: 0.004,
    count: 3,
  },
  {
    name: "Carbaryl",
    mean: 0.01,
    min: 0.01,
    max: 0.02,
    stdDev: 0.003,
    count: 2,
  },
  {
    name: "Paraquat",
    mean: 0.04,
    min: 0.03,
    max: 0.05,
    stdDev: 0.008,
    count: 6,
  },
])

// Pagination setup
const itemsPerPage = 3
const currentPage = ref(1)

const totalPages = computed(() =>
  Math.ceil(allChemicals.value.length / itemsPerPage)
)

const paginatedChemicals = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return allChemicals.value.slice(start, end)
})

function nextPage() {
  if (currentPage.value < totalPages.value) {
    currentPage.value++
  }
}

function prevPage() {
  if (currentPage.value > 1) {
    currentPage.value--
  }
}

const countries = ref<types.Option[]>([
  { name: "All" },
  { name: "Albania", isoAlpha2: "AL" },
  { name: "Andorra", isoAlpha2: "AD" },
  { name: "Armenia", isoAlpha2: "AM" },
  { name: "Austria", isoAlpha2: "AT" },
  { name: "Azerbaijan", isoAlpha2: "AZ" },
  { name: "Belarus", isoAlpha2: "BY" },
  { name: "Belgium", isoAlpha2: "BE" },
  { name: "Bosnia and Herzegovina", isoAlpha2: "BA" },
  { name: "Bulgaria", isoAlpha2: "BG" },
  { name: "Croatia", isoAlpha2: "HR" },
  { name: "Cyprus", isoAlpha2: "CY" },
  { name: "Czech Republic", isoAlpha2: "CZ" },
  { name: "Denmark", isoAlpha2: "DK" },
  { name: "Estonia", isoAlpha2: "EE" },
  { name: "Finland", isoAlpha2: "FI" },
  { name: "France", isoAlpha2: "FR" },
  { name: "Georgia", isoAlpha2: "GE" },
  { name: "Germany", isoAlpha2: "DE" },
  { name: "Greece", isoAlpha2: "GR" },
  { name: "Hungary", isoAlpha2: "HU" },
  { name: "Iceland", isoAlpha2: "IS" },
  { name: "Ireland", isoAlpha2: "IE" },
  { name: "Italy", isoAlpha2: "IT" },
  { name: "Kazakhstan", isoAlpha2: "KZ" },
  { name: "Kosovo", isoAlpha2: "XK" },
  { name: "Latvia", isoAlpha2: "LV" },
  { name: "Liechtenstein", isoAlpha2: "LI" },
  { name: "Lithuania", isoAlpha2: "LT" },
  { name: "Luxembourg", isoAlpha2: "LU" },
  { name: "Malta", isoAlpha2: "MT" },
  { name: "Moldova", isoAlpha2: "MD" },
  { name: "Monaco", isoAlpha2: "MC" },
  { name: "Montenegro", isoAlpha2: "ME" },
  { name: "Netherlands", isoAlpha2: "NL" },
  { name: "North Macedonia", isoAlpha2: "MK" },
  { name: "Norway", isoAlpha2: "NO" },
  { name: "Poland", isoAlpha2: "PL" },
  { name: "Portugal", isoAlpha2: "PT" },
  { name: "Romania", isoAlpha2: "RO" },
  { name: "Russia", isoAlpha2: "RU" },
  { name: "San Marino", isoAlpha2: "SM" },
  { name: "Serbia", isoAlpha2: "RS" },
  { name: "Slovakia", isoAlpha2: "SK" },
  { name: "Slovenia", isoAlpha2: "SI" },
  { name: "Spain", isoAlpha2: "ES" },
  { name: "Sweden", isoAlpha2: "SE" },
  { name: "Switzerland", isoAlpha2: "CH" },
  { name: "Turkey", isoAlpha2: "TR" },
  { name: "Ukraine", isoAlpha2: "UA" },
  { name: "United Kingdom", isoAlpha2: "GB" },
  { name: "Vatican City", isoAlpha2: "VA" },
])

const decades = ref<{ name: string }[]>([
  { name: "All" },
  { name: "1900-1910" },
  { name: "1910-1920" },
  { name: "1920-1930" },
  { name: "1930-1940" },
  { name: "1940-1950" },
  { name: "1950-1960" },
  { name: "1960-1970" },
  { name: "1970-1980" },
  { name: "1980-1990" },
  { name: "1990-2000" },
  { name: "2000-2010" },
  { name: "2010-2020" },
  { name: "2020-2030" },
])

const chemicals = ref<types.Option[]>([
  { name: "All" },
  { name: "Tetrachloroethylene", code: "CAS_127-18-4" },
  { name: "Trichloroethylene", code: "CAS_79-01-6" },
  { name: "Perchloroethylene", code: "CAS_127-18-4" },
  { name: "Chloroform", code: "CAS_67-66-3" },
  { name: "Dichloromethane", code: "CAS_75-09-2" },
  { name: "Carbon Tetrachloride", code: "CAS_56-23-5" },
  { name: "1,1,1-Trichloroethane", code: "CAS_71-55-6" },
  { name: "Methylene Chloride", code: "CAS_75-09-2" },
  { name: "Tetrachloromethane", code: "CAS_56-23-5" },
  { name: "Bromotrichloromethane", code: "CAS_75-64-9" },
  { name: "Perfluorocyclopropane", code: "CAS_675-99-2" },
  { name: "Hexachloroethane", code: "CAS_67-72-1" },
])

const data = ref<types.BarData[]>([
  { x: "Trichloromethane", y: 5 },
  { x: "Fenthion", y: 3 },
  { x: "Chloridazon", y: 1 },
  { x: "Thallium", y: 2 },
])
</script>