<script setup lang="ts">
//@ts-ignore
import Europe from "./EuropeMap.vue"
import { onMounted, ref } from 'vue';

interface Country { country: string; isoAlpha2: string, clicked: boolean }

const selectedCountry = ref<Country | null>(null)

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
              selectedCountry.value = null
            } else {
              europeanCountries.forEach(otherCountry => {
                if (otherCountry.clicked) {
                  const otherPath = document.getElementById(`${otherCountry.isoAlpha2.toLowerCase()}`);
                  if (otherPath) {
                    otherPath.classList.remove('fill-ocean');
                    otherPath.classList.add('fill-gray-200');
                    otherCountry.clicked = false;
                  }
                }
              });

              selectedCountry.value = country
              path.classList.remove('fill-gray-200');
              path.classList.add('fill-ocean');
              country.clicked = true;

            }
          }
        });
      } else {
        path.classList.add('fill-gray-200', 'stroke-gray-600');
      }
    });
  } else {
    console.error('No paths found inside #countries');
  }
});

const comparison = ref(false)

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
    <div class="flex flex-col items-center justify-center w-full h-full" v-if="!selectedCountry">
      <div class="py-12 text-ocean text-lg">
        <span class="font-semibold">Select a country </span>
        <span class="font-normal">to explore its water quality metrics in detail.</span>
      </div>
      <div class="py-12 text-ocean text-sm">
        <div class="pb-2">Want to <span class="font-semibold">compare</span> two countries?</div>
        <div class="py-4">Enable comparison mode using the button below and click on two countries to see side-by-side insights into their water quality data.        </div>
        <div @click="comparison = !comparison" class="px-3 py-2 bg-ocean text-white w-fit rounded-lg shadow font-semibold hover:bg-gray-400 hover:cursor-pointer">Compare</div>
      </div>
    </div>
    <div class="flex flex-col items-start justify-start w-full h-full" v-if="selectedCountry">
      <div class="font-semibold text-ocean text-lg">{{ selectedCountry?.country }}</div>
    </div>
    
   </div>
</div>

</template>
