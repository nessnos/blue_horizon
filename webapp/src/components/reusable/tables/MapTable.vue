<template>
  <!-- If more than one country is selected -->
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
        <tbody>
          <template
            v-for="(label, index) in [
              'Total Monitoring Sites',
              'Decades Covered',
              'Water Body Category',
              'Matrix',
              'Count of Chemicals Monitored',
              'Number of Collected Samples',
              'Proportion Of Confirmed Samples',
              'Percentage of Missing Data',
            ]"
            :key="'general-' + index"
          >
            <!-- Label Row -->
            <tr>
              <td
                :colspan="selectedCountry.length"
                class="border border-gray-300 bg-gray-100 p-2 text-center text-sm font-semibold text-ocean"
              >
                {{ label }}
              </td>
            </tr>
            <!-- Data Row -->
            <tr>
              <td
                v-for="(_, countryIndex) in selectedCountry"
                :key="countryIndex"
                class="border border-gray-300 p-2 text-center text-xs text-ocean"
              >
                {{ getGeneralInfo(label) }}
              </td>
            </tr>
          </template>

          <template
            v-for="(label, index) in [
              'Most Monitored Determinand',
              'Mean Concentration',
              'Maximum Recorded Value',
              'Minimum Recorded Value',
              'Standard Deviation',
              'Total Samples',
            ]"
            :key="'quality-' + index"
          >
            <!-- Label Row -->
            <tr>
              <td
                :colspan="selectedCountry.length"
                class="border border-gray-300 bg-gray-100 p-2 text-center text-sm font-semibold text-ocean"
              >
                {{ label }}
              </td>
            </tr>
            <!-- Data Row -->
            <tr>
              <td
                v-for="(_, countryIndex) in selectedCountry"
                :key="countryIndex"
                class="border border-gray-300 p-2 text-center text-xs text-ocean"
              >
                {{ getQualityInfo(label) }}
              </td>
            </tr>
          </template>
        </tbody>
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
import DefaultButton from "@/components/reusable/buttons/DefaultButton.vue"
import { RouterLink } from "vue-router"
</script>
