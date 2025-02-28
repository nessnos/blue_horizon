<template>
  <tbody v-for="(label, index) in labels" :key="'general-' + index">
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
        {{ info(label) }}
      </td>
    </tr>
  </tbody>
</template>

<script lang="ts" setup>
import { defineProps } from "vue"
import type { Country } from "@/type"

defineProps<{
  labels: string[]
  selectedCountry: Country[]
  info: any
}>()
</script>
