<script setup lang="ts">
import { RouterView, RouterLink, useRoute, useRouter } from "vue-router"
//@ts-ignore
import Europe from "./EuropeMap.vue";
import { ExclamationCircleIcon } from "@heroicons/vue/24/solid";
import { onMounted, ref } from 'vue';
import { Switch } from '@headlessui/vue';
import { TransitionRoot, TransitionChild, Dialog, DialogPanel, DialogTitle } from '@headlessui/vue'
import type { Country } from "@/type";

const selectedCountry = ref<Country[]>([])

const europeanCountries: Country[] = [
  { country: "Albania", isoAlpha2: "AL", clicked : false },
  { country: "Andorra", isoAlpha2: "AD", clicked : false },
  { country: "Armenia", isoAlpha2: "AM", clicked : false },
  { country: "Austria", isoAlpha2: "AT", clicked : false },
  { country: "Azerbaijan", isoAlpha2: "AZ", clicked : false },
  { country: "Belarus", isoAlpha2: "BY", clicked : false },
  { country: "Belgium", isoAlpha2: "BE", clicked : false },
  { country: "Bosnia and Herzegovina", isoAlpha2: "BA", clicked : false },
  { country: "Bulgaria", isoAlpha2: "BG", clicked : false },
  { country: "Croatia", isoAlpha2: "HR", clicked : false },
  { country: "Cyprus", isoAlpha2: "CY", clicked : false },
  { country: "Czech Republic", isoAlpha2: "CZ", clicked : false },
  { country: "Denmark", isoAlpha2: "DK", clicked : false },
  { country: "Estonia", isoAlpha2: "EE", clicked : false },
  { country: "Finland", isoAlpha2: "FI", clicked : false },
  { country: "France", isoAlpha2: "FR", clicked : false },
  { country: "Georgia", isoAlpha2: "GE", clicked : false },
  { country: "Germany", isoAlpha2: "DE", clicked : false },
  { country: "Greece", isoAlpha2: "GR", clicked : false },
  { country: "Hungary", isoAlpha2: "HU", clicked : false },
  { country: "Iceland", isoAlpha2: "IS", clicked : false },
  { country: "Ireland", isoAlpha2: "IE", clicked : false },
  { country: "Italy", isoAlpha2: "IT", clicked : false },
  { country: "Kosovo", isoAlpha2: "XK", clicked : false },
  { country: "Latvia", isoAlpha2: "LV", clicked : false },
  { country: "Liechtenstein", isoAlpha2: "LI", clicked : false },
  { country: "Lithuania", isoAlpha2: "LT", clicked : false },
  { country: "Luxembourg", isoAlpha2: "LU", clicked : false },
  { country: "Malta", isoAlpha2: "MT", clicked : false },
  { country: "Moldova", isoAlpha2: "MD", clicked : false },
  { country: "Monaco", isoAlpha2: "MC", clicked : false },
  { country: "Montenegro", isoAlpha2: "ME", clicked : false },
  { country: "Netherlands", isoAlpha2: "NL", clicked : false },
  { country: "North Macedonia", isoAlpha2: "MK", clicked : false },
  { country: "Norway", isoAlpha2: "NO", clicked : false },
  { country: "Poland", isoAlpha2: "PL", clicked : false },
  { country: "Portugal", isoAlpha2: "PT", clicked : false },
  { country: "Romania", isoAlpha2: "RO", clicked : false },
  { country: "Russia", isoAlpha2: "RU", clicked : false },
  { country: "San Marino", isoAlpha2: "SM", clicked : false },
  { country: "Serbia", isoAlpha2: "RS", clicked : false },
  { country: "Slovakia", isoAlpha2: "SK", clicked : false },
  { country: "Slovenia", isoAlpha2: "SI", clicked : false },
  { country: "Spain", isoAlpha2: "ES", clicked : false },
  { country: "Sweden", isoAlpha2: "SE", clicked : false },
  { country: "Switzerland", isoAlpha2: "CH", clicked : false },
  { country: "Turkey", isoAlpha2: "TR", clicked : false },
  { country: "Ukraine", isoAlpha2: "UA", clicked : false },
  { country: "United Kingdom", isoAlpha2: "GB", clicked : false },
  { country: "Vatican City", isoAlpha2: "VA", clicked : false },
];


const getGeneralInfo = (label: string): string => {
  const data: Record<string, string> = {
    "Total Monitoring Sites": "3",
    "Decades Covered": "1920 - 2023",
    "Water Body Category": "Rivers and Lakes",
    "Matrix": "Water",
    "Count of Chemicals Monitored": "6",
    "Number of Collected Samples": "6",
    "Proportion Of Confirmed Samples": "6%",
    "Percentage of Missing Data": "6%"
  };
  
  return data[label] || "-";
};

const getQualityInfo = (label: string): string => {
  const data: Record<string, string> = {
    "Most Monitored Determinand": "Tetrachloroethylene (CAS_127-18-4)",
    "Mean Concentration": "0.052 µg/L",
    "Maximum Recorded Value": "0.12 µg/L",
    "Minimum Recorded Value": "0.02 µg/L",
    "Standard Deviation": "0.015 µg/L",
    "Total Samples": "100"
  };
  
  return data[label] || "-";
};

  

onMounted(() => {
  const paths = document.querySelectorAll('#countries path');
  
  if (paths.length > 0) {
    paths.forEach((path) => {
      const isoAlpha2 = path.getAttribute('id')?.toString().toUpperCase();
      const isEuropean = europeanCountries.some(country => country.isoAlpha2 === isoAlpha2);

      if (isEuropean) {
        path.classList.add('fill-gray-200', 'stroke-gray-600', 'hover:fill-ocean', 'hover:cursor-pointer');
        
        path.addEventListener('click', function (e) {
          const country = europeanCountries.find(country => country.isoAlpha2 === isoAlpha2);

          if (country) {
            if (country.clicked) {
              path.classList.remove('fill-ocean');
              path.classList.add('fill-gray-200');
              country.clicked = false;
              selectedCountry.value.splice(selectedCountry.value.indexOf(country), 1);
            } 
            else if(comparison.value) {
              const numberClicked = europeanCountries.filter(function(s) { return s.clicked; }).length
              if(numberClicked == 2){
                console.error("you can't select more than 2 countries")
                isOpen.value = true
              }
              else{
                path.classList.remove('fill-gray-200');
                path.classList.add('fill-ocean');
                country.clicked = true;
                selectedCountry.value.push(country)
              }
            }
            else {
              europeanCountries.forEach(otherCountry => {
                if (otherCountry.clicked) {
                  const otherPath = document.getElementById(`${otherCountry.isoAlpha2.toLowerCase()}`);
                  if (otherPath) {
                    otherPath.classList.remove('fill-ocean');
                    otherPath.classList.add('fill-gray-200');
                    otherCountry.clicked = false;
                    selectedCountry.value.splice(selectedCountry.value.indexOf(country), 1);
                  }
                }
                path.classList.remove('fill-gray-200');
                path.classList.add('fill-ocean');
                country.clicked = true;
              });

              selectedCountry.value.push(country)
              

            }
          }
        });
      } else {
        path.classList.add('fill-gray-400', 'stroke-gray-600');
      }
    });
  } else {
    console.error('No paths found inside #countries');
  }
});

const comparison = ref(false)
const isOpen = ref(false)

const resetComparison = () => {
  const selectedAll = europeanCountries.filter(function(s) { return s.clicked; })
  selectedAll.forEach(country => {
    const otherPath = document.getElementById(`${country.isoAlpha2.toLowerCase()}`);
    if (otherPath) {
        otherPath.classList.remove('fill-ocean');
        otherPath.classList.add('fill-gray-200');
        country.clicked = false;
        selectedCountry.value.splice(selectedCountry.value.indexOf(country), 1);
      }
  })
  isOpen.value = !isOpen.value
}
</script>

<template>
<div class="grid grid-cols-4 h-full items-start justify-start">
   <div class="col-span-3 flex flex-col justify-start items-start h-full w-full">
    <Europe class="w-full mb-4"/>
    <div class="py-1 p-4 text-gray-500 font-normal text-xs">Comparison Mode : 
      <span v-if="comparison">On</span>
      <span v-else>Off</span>
    </div>  
   </div>
   <div class="h-full overflow-scroll">
    <div class="px-6 py-4 flex flex-col items-center justify-center w-full h-full" v-if="!selectedCountry.length">
      <div v-if="!comparison" class="min-h-56 py-12 text-ocean text-lg">
        <span class="font-semibold">Select a country </span>
        <span class="font-normal">to explore its water quality metrics in detail.</span>
      </div>
      <div v-else class="min-h-56 py-12 text-ocean text-lg">
        <span class="font-semibold">Select two countries </span>
        <span class="font-normal">to explore their water quality metrics in detail and compare.</span>
      </div>
      <div class="py-12 text-ocean text-sm">
        <div class="flex flex-row w-full items-end justify-start gap-5 pb-2">
          <div>Want to <span class="font-semibold">compare</span> two countries?</div>
          <Switch
            v-model="comparison"
            :class="comparison ? 'bg-ocean' : 'bg-gray-300'"
            class="relative inline-flex h-[18px] w-[34px] shrink-0 cursor-pointer rounded-full border-2 border-transparent transition-colors duration-200 ease-in-out focus:outline-none focus-visible:ring-2 focus-visible:ring-white/75"
          >
            <span
              aria-hidden="true"
              :class="comparison ? 'translate-x-4' : 'translate-x-0'"
              class="pointer-events-none inline-block h-[14px] w-[14px] transform rounded-full bg-white shadow-lg ring-0 transition duration-200 ease-in-out"
            />
          </Switch>
        </div>
        <div class="py-4">Enable comparison mode using the switch above and click on two countries to see side-by-side insights into their water quality data.        </div>
      </div>
    </div>
    <div class="w-full h-full" v-if="selectedCountry.length">
      <!-- If more than one country is selected -->
      <div class="w-full h-full" v-if="selectedCountry.length > 1">
        <div class="w-fit min-w-full">
          <table class="w-full border border-gray-300">
            <thead>
              <tr class="h-12">
                <th v-for="(country, index) in selectedCountry" :key="index" class="font-bold text-lg p-2 border border-gray-300 text-ocean">
                  {{ country.country }}
                </th>
              </tr>
            </thead>
            <tbody>
              <template v-for="(label, index) in [
                'Total Monitoring Sites',
                'Decades Covered', 
                'Water Body Category',
                'Matrix',
                'Count of Chemicals Monitored',
                'Number of Collected Samples',
                'Proportion Of Confirmed Samples',
                'Percentage of Missing Data'
              ]" :key="'general-' + index">
                <!-- Label Row -->
                <tr>
                  <td class="border border-gray-300 text-sm p-2 font-semibold text-center bg-gray-100 text-ocean" 
                      :colspan="selectedCountry.length">
                    {{ label }}
                  </td>
                </tr>
                <!-- Data Row -->
                <tr>
                  <td v-for="(_, countryIndex) in selectedCountry" :key="countryIndex" 
                      class="border border-gray-300 p-2 text-center text-xs text-ocean">
                    {{ getGeneralInfo(label) }}
                  </td>
                </tr>
              </template>

              <template v-for="(label, index) in [
                'Most Monitored Determinand',
                'Mean Concentration',
                'Maximum Recorded Value',
                'Minimum Recorded Value',
                'Standard Deviation',
                'Total Samples'
              ]" :key="'quality-' + index">
                <!-- Label Row -->
                <tr>
                  <td class="border border-gray-300 text-sm p-2 font-semibold text-center bg-gray-100 text-ocean" 
                      :colspan="selectedCountry.length">
                    {{ label }}
                  </td>
                </tr>
                <!-- Data Row -->
                <tr>
                  <td v-for="(_, countryIndex) in selectedCountry" :key="countryIndex" 
                      class="border border-gray-300 p-2 text-center text-xs text-ocean">
                    {{ getQualityInfo(label) }}
                  </td>
                </tr>
              </template>
            </tbody>
          </table>
          <div class="py-6 flex flex-row gap-12 items-start justify-between px-4">
            <RouterLink :to="{name : 'dashboard', query : { country: country.country } }" v-for="country in selectedCountry" class="text-center w-fit bg-ocean px-3 py-2 rounded-lg shadow text-xs text-white hover:cursor-pointer">
              Explore {{ country.country }}
            </RouterLink>
          </div>
        </div>
      </div>

      <!-- If only one country is selected -->
      <div class="w-full h-full" v-else>
        <div class="w-fit min-w-full">
          <table class="w-full">
            <thead>
              <tr>
                <th class="text-ocean text-lg h-12 gont-bold">
                  {{ selectedCountry[0].country }} ({{ selectedCountry[0].isoAlpha2 }})
                </th>
              </tr>
            </thead>
            <tbody>
              <template v-for="(label, index) in [
                'Total Monitoring Sites',
                'Decades Covered', 
                'Water Body Category',
                'Matrix',
                'Count of Chemicals Monitored',
                'Number of Collected Samples',
                'Proportion Of Confirmed Samples',
                'Percentage of Missing Data'
              ]" :key="'general-' + index">
                <!-- Label Row -->
                <tr>
                  <td class="border border-gray-300 text-sm p-2 font-semibold text-center text-ocean">
                    {{ label }}
                  </td>
                </tr>
                <!-- Data Row -->
                <tr>
                  <td class="border border-gray-300 p-2 text-center text-xs bg-gray-100 text-ocean">
                    {{ getGeneralInfo(label) }}
                  </td>
                </tr>
              </template>

              <template v-for="(label, index) in [
                'Most Monitored Determinand',
                'Mean Concentration',
                'Maximum Recorded Value',
                'Minimum Recorded Value',
                'Standard Deviation',
                'Total Samples'
              ]" :key="'quality-' + index">
                <!-- Label Row -->
                <tr>
                  <td class="border border-gray-300 text-sm p-2 font-semibold text-center text-ocean">
                    {{ label }}
                  </td>
                </tr>
                <!-- Data Row -->
                <tr>
                  <td class="border border-gray-300 p-2 text-center text-xs bg-gray-100 text-ocean">
                    {{ getQualityInfo(label) }}
                  </td>
                </tr>
              </template>
            </tbody>
          </table>
          <div class="py-6 flex justify-center">
            <RouterLink :to="{name : 'dashboard', query : { country: selectedCountry[0].country } }" class="bg-ocean px-3 py-2 rounded-lg shadow text-xs text-white hover:cursor-pointer">
              Explore More
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>


<TransitionRoot appear :show="isOpen" as="template">
    <Dialog as="div" @close="isOpen = !isOpen" class="relative z-10">
      <TransitionChild
        as="template"
        enter="duration-300 ease-out"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="duration-200 ease-in"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div class="fixed inset-0 bg-black/25" />
      </TransitionChild>

      <div class="fixed inset-0 overflow-y-auto">
        <div
          class="flex min-h-full items-center justify-center p-4 text-center"
        >
          <TransitionChild
            as="template"
            enter="duration-300 ease-out"
            enter-from="opacity-0 scale-95"
            enter-to="opacity-100 scale-100"
            leave="duration-200 ease-in"
            leave-from="opacity-100 scale-100"
            leave-to="opacity-0 scale-95"
          >
            <DialogPanel
              class="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all"
            >
              <DialogTitle
                as="h3"
                class="flex flex-row items-center gap-2 text-lg font-medium leading-6 text-red-700"
              >
                <ExclamationCircleIcon class="h-6 w-6" />
                <span>Selection Error</span>
              </DialogTitle>
              <div class="mt-6">
                <div class="text-sm text-gray-500">
                  You can only select up to two countries at a time for comparison. 
                  Please deselect all or one country to choose a new one.
                </div>
              </div>

              <div class="mt-8 flex flex-row justify-between items-center">
                <button
                  type="button"
                  class="inline-flex justify-center rounded-md border border-transparent bg-red-100 px-4 py-2 text-sm font-medium text-red-900 hover:bg-red-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                  @click="resetComparison"
                >
                  Deselect All
                </button>
                <button
                  type="button"
                  class="inline-flex justify-center rounded-md border border-transparent bg-blue-100 px-4 py-2 text-sm font-medium text-blue-900 hover:bg-blue-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                  @click="isOpen = !isOpen"
                >
                  Let Me Choose
                </button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
  </TransitionRoot>
</template>
