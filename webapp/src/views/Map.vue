<script setup lang="ts">
//@ts-ignore
import Europe from "./EuropeMap.vue";
import { ExclamationCircleIcon } from "@heroicons/vue/24/solid";
import { onMounted, ref } from 'vue';
import { Switch } from '@headlessui/vue';
import { TransitionRoot, TransitionChild, Dialog, DialogPanel, DialogTitle } from '@headlessui/vue'

interface Country { country: string; isoAlpha2: string, clicked: boolean }

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
  { country: "Kazakhstan", isoAlpha2: "KZ", clicked : false },
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
   <div class="p-6 h-full bg-white border-l-2 border-gray-300">
    <div class="flex flex-col items-center justify-center w-full h-full" v-if="!selectedCountry.length">
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
    <div class="flex flex-col items-start justify-start w-full h-full" v-if="selectedCountry">
      <div v-for="country in selectedCountry">
        <div class="font-bold text-ocean text-xl py-2 pb-3">{{ country.country }} ({{ country.isoAlpha2 }})</div>
        <div class="font-bold text-sm py-2 text-ocean">General Information</div>
        <div class="pl-2">
          <div class="text-xs font-semibold text-ocean">Total Monitoring Sites : <span class="font-normal">6</span></div>
          <div class="text-xs font-semibold text-ocean">Decades Covered : <span class="font-normal">1920 - 2023</span></div>
          <div class="text-xs font-semibold text-ocean">Water Body Category : <span class="font-normal">Rivers and Lakes</span></div>
          <div class="text-xs font-semibold text-ocean">Matrix : <span class="font-normal">Water</span></div>
        </div>

        <div class="font-bold text-sm py-2 text-ocean">Water Quality Measures</div>
        <div class="pl-2">    
          <div class="text-xs font-semibold text-ocean">Most Monitored Determinand : <span class="font-normal">Tetrachloroethylene (CAS_127-18-4)</span></div>     
          <div class="text-xs font-semibold text-ocean">Mean Concentration : <span class="font-normal">0.052 µg/L</span></div>
          <div class="text-xs font-semibold text-ocean">Maximum Recorded Value : <span class="font-normal">0.12 µg/L</span></div>
          <div class="text-xs font-semibold text-ocean">Minimum Recorded Value : <span class="font-normal">0.02 µg/L</span></div>
          <div class="text-xs font-semibold text-ocean">Standard Deviation : <span class="font-normal">0.015 µg/L</span></div>
          <div class="text-xs font-semibold text-ocean">Total Samples : <span class="font-normal">100</span></div>
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
