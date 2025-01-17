<script setup lang="ts">
//@ts-ignore
import Europe from "./EuropeMap.vue"
import { onMounted } from 'vue';

const europeanCountries: { country: string; isoAlpha2: string, clicked: boolean }[] = [
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
            } else {
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



</script>
<template>

<div class="flex flex-row items-start justify-start">
   <Europe class="h-full"/>
   <div class="p-6 h-full bg-white border-l-2 border-gray-300">
      <div class="font-semibold text-ocean text-lg">Select a country</div>
   </div>
</div>

</template>
