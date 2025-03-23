<template>
  <tbody v-for="(label, index) in labels" :key="index">
    <!-- Label Row -->
    <tr>
      <td :colspan="selectedCountry.length"
        class="border border-gray-300 bg-gray-100 p-2 text-center text-sm font-semibold text-ocean">
        {{ label }}
      </td>
    </tr>
    <!-- Data Row -->
    <tr>
      <td v-for="(country, countryIndex) in selectedCountry" :key="countryIndex"
        v-if="info && Object.keys(info).length > 0" class="border border-gray-300 p-2 text-center text-xs text-ocean">
        {{ formatValue(info?.[country.code]?.[label]) }} 
        <span v-if="typeof info?.[country.code]?.[label] === 'number' && !['Total des sites surveillés', 'Total des propriétés observées','Total des échantillons collectés','Taux d\'échantillons confirmés', 'Nombre total d\'échantillons'].includes(label)">
          {{info?.[country.code]?.['Unité de Mesure']}}
        </span>
        <span v-if="label == 'Taux d\'échantillons confirmés'">
          %
        </span>
      </td>
    </tr>
  </tbody> 
</template>

<script lang="ts" setup>
import type * as types from "@/type"

defineProps<{
  labels: string[]
  selectedCountry: types.Country[]
  info?: { [key: string]: types.CountryGeneralInfo };
}>()

const formatValue = (value: any) => {
  return typeof value === "number" 
    ? value.toLocaleString("fr-BE", { maximumFractionDigits: 2 }) 
    : value;
}
</script>
