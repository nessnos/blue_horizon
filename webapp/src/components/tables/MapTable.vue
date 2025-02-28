<template>
  <div class="w-full">
    <div class="w-fit min-w-full">
      <table class="w-full border border-gray-300">
        <thead>
          <tr class="h-12">
            <th
              v-for="(country, index) in selectedCountry"
              :key="index"
              class="border border-gray-300 p-2 text-lg font-bold text-ocean"
            >
              {{ country.country }}
            </th>
          </tr>
        </thead>
        <CountryTable
          :info="generalInfo"
          :labels="[
            'Total Monitoring Sites',
            'Decades Covered',
            'Water Body Category',
            'Matrix',
            'Count of Chemicals Monitored',
            'Number of Collected Samples',
            'Proportion Of Confirmed Samples',
            'Percentage of Missing Data',
          ]"
          :selected-country="selectedCountry"
        />
        <CountryTable
          :info="qualityInfo"
          :labels="[
            'Most Monitored Determinand',
            'Mean Concentration',
            'Maximum Recorded Value',
            'Minimum Recorded Value',
            'Standard Deviation',
            'Total Samples',
          ]"
          :selected-country="selectedCountry"
        />
      </table>
      <div class="flex flex-row items-start justify-between gap-12 px-4 py-6">
        <RouterLink
          v-for="country in selectedCountry"
          :to="{ name: 'dashboard', query: { country: country.country } }"
          class="w-fit rounded-lg bg-ocean px-3 py-2 text-center text-xs text-white shadow hover:cursor-pointer"
        >
          Explore {{ country.country }}
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { RouterLink } from "vue-router"
import { defineProps } from "vue"
import type { Country } from "@/type"
import CountryTable from "@/components/tables/CountryTable.vue"

defineProps<{
  selectedCountry: Country[]
  qualityInfo: any
  generalInfo: any
}>()
</script>
