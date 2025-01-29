<script setup lang="ts">
import { ref } from 'vue'
import type * as types from "@/type";
import SelectOption from "@/assets/reusable/Dropdowns/SelectOption.vue"
//@ts-ignore
import BarChart from '@/assets/reusable/Charts/BarChart.vue';
import DonutChart from '@/assets/reusable/Charts/DonutChart.vue';
import LineChart from '@/assets/reusable/Charts/LineChart.vue';
//@ts-ignore
import Chemicals from '@/assets/icons/Chemicals.vue';
import WebDomain from '@/assets/icons/WebDomain.vue';
import Sample from '@/assets/icons/Sample.vue';
import MissingData from '@/assets/icons/MissingData.vue';
import Proportion from '@/assets/icons/Proportion.vue';

const countries = ref<types.Option[]>([
  {name: 'All'},
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
]);

const decades = ref<{ name: string }[]>([
  {name : 'All'},
  { name: '1900-1910' },
  { name: '1910-1920' },
  { name: '1920-1930' },
  { name: '1930-1940' },
  { name: '1940-1950' },
  { name: '1950-1960' },
  { name: '1960-1970' },
  { name: '1970-1980' },
  { name: '1980-1990' },
  { name: '1990-2000' },
  { name: '2000-2010' },
  { name: '2010-2020' },
  { name: '2020-2030' },
]);

const chemicals = ref<types.Option[]>([
  {name : 'All'},
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
  { name: "Hexachloroethane", code: "CAS_67-72-1" }
]);


const data = ref<types.BarData[]>([
    { "x": "Trichloromethane", "y": 5 },
    { "x": "Fenthion", "y": 3 },
    { "x": "Chloridazon", "y": 1 },
    { "x": "Thallium", "y": 2 }
]
)

</script>
<template>
    <div class="p-12 w-full h-full flex flex-col items-start justify-between">
        <div class="flex flex-row gap-3">
            <SelectOption
                :rowData="countries"
                :label="'Country'"
            />
            <SelectOption
                :rowData="decades"
                :label="'Decades'"
            />
            <SelectOption
                :rowData="chemicals"
                :label="'Chemicals'"
            />
        </div>
        <div class="py-6 flex flex-row justify-between items-center w-full">
          <div class="p-3 px-4 bg-aqua/25 text-ocean shadow-lg rounded-lg h-fit min-h-24 w-56">
            <div class="flex flex-col gap-8 items-start">
              <div class="flex flex-row items-center justify-between w-full">
                <Chemicals class="fill-ocean bg-aqua/35 p-2 rounded-lg w-10 h-10"/>
                <div class="font-bold text-2xl pr-6">6</div>
              </div>
              <div class="font-normal text-xs">Count of Chemicals Monitored</div>
            </div>
          </div>
          <div class="p-3 px-4 bg-aqua/25 text-ocean shadow-lg rounded-lg h-fit min-h-24 w-56">
            <div class="flex flex-col gap-8 items-start">
              <div class="flex flex-row items-center justify-between w-full">
                <WebDomain class="fill-ocean bg-aqua/35 p-2 rounded-lg w-10 h-10"/>
                <div class="font-bold text-2xl pr-6">2</div>
              </div>
              <div class="font-normal text-xs">Count of Monitoring Sites</div>
            </div>
          </div>
          <div class="p-3 px-4 bg-aqua/25 text-ocean shadow-lg rounded-lg h-fit min-h-24 w-56">
            <div class="flex flex-col gap-8 items-start">
              <div class="flex flex-row items-center justify-between w-full">
                <Sample class="fill-ocean bg-aqua/35 p-2 rounded-lg w-10 h-10"/>
                <div class="font-bold text-2xl pr-6">256</div>
              </div>
              <div class="font-normal text-xs">Number of Collected Samples</div>
            </div>
          </div>
          <div class="p-3 px-4 bg-aqua/25 text-ocean shadow-lg rounded-lg h-fit min-h-24 w-56">
            <div class="flex flex-col gap-8 items-start">
              <div class="flex flex-row items-center justify-between w-full">
                <Proportion class="fill-ocean bg-aqua/35 p-2 rounded-lg w-10 h-10"/>
                <div class="font-bold text-2xl pr-6">2<span class="pl-1 text-xs">%</span></div>
              </div>
              <div class="text-left font-normal text-xs">Proportion Of Confirmed Samples</div>
            </div>
          </div>
          <div class="p-3 px-4 bg-aqua/25 text-ocean shadow-lg rounded-lg h-fit min-h-24 w-56">
            <div class="flex flex-col gap-8 items-start">
              <div class="flex flex-row items-center justify-between w-full">
                <MissingData class="fill-ocean bg-aqua/35 p-2 rounded-lg w-10 h-10"/>
                <div class="font-bold text-2xl pr-6">25<span class="pl-1 text-xs">%</span></div>
              </div>
              <div class="font-normal text-xs">Percentage of Missing Data</div>
            </div>
          </div>
        </div>
        <div class="w-full flex flex-row gap-12 items-start">
          <div class="w-40 h-40 mr-8">
            <DonutChart :chartData="data"/>
          </div>
          <div class="min-w-2/3 w-full h-full min-h-fit">
            <table class="w-full bg-white rounded-lg shadow text-xs">
                <thead>
                    <tr class="border-b border-ocean text-gray-700 rounded-lg">
                        <th class="px-4 py-2">Chemical Name</th>
                        <th class="px-4 py-2">Mean</th>
                        <th class="px-4 py-2">Min</th>
                        <th class="px-4 py-2">Max</th>
                        <th class="px-4 py-2">Std Dev</th>
                        <th class="px-4 py-2">Median</th>
                        <th class="px-4 py-2">Count</th>
                    </tr>
                </thead>
                <tbody>
                    <!-- Example Row (Replace with dynamic content) -->
                    <tr class="text-center">
                        <td class="px-4 py-2">Trichloromethane</td>
                        <td class="px-4 py-2">0.01</td>
                        <td class="px-4 py-2">0.01</td>
                        <td class="px-4 py-2">0.02</td>
                        <td class="px-4 py-2">0.005</td>
                        <td class="px-4 py-2">0.01</td>
                        <td class="px-4 py-2">5</td>
                    </tr>
                    <tr class="text-center bg-gray-50/25">
                        <td class="px-4 py-2">Fenthion</td>
                        <td class="px-4 py-2">0.02</td>
                        <td class="px-4 py-2">0.01</td>
                        <td class="px-4 py-2">0.03</td>
                        <td class="px-4 py-2">0.007</td>
                        <td class="px-4 py-2">0.02</td>
                        <td class="px-4 py-2">4</td>
                    </tr>
                    <!-- Add more rows dynamically -->
                </tbody>
            </table>
          </div>
        </div>
        <div class="w-full flex flex-row justify-between items-center">
          <div class="w-1/2 h-64 px-6">
            <LineChart :chartData="data"/>
          </div>
          <div class="w-1/2 h-64 px-6">
            <BarChart :chartData="data"/>
          </div>
        </div>
    </div>
</template>