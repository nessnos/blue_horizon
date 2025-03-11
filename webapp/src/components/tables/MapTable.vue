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
              <div class="flex flex-row items-center gap-3 justify-center">
                <span class="fi rounded-[0.2rem] shadow" :class="'fi-' + country.code?.toLowerCase()"></span>
                <span>{{ country.name }}</span>
              </div>
            </th>
          </tr>
        </thead>
        <CountryTable
          v-if="Object.keys(generalInfo).length > 0"
          :info="generalInfo"
          :labels="[
            'Total des sites surveillés',
            'Décennies',
            'Catégorie des corps d\'eau',
            'Matrice',
            'Total des propriétés observées',
            'Total des échantillons collectés',
            'Taux d\'échantillons confirmés',
            'Le déterminant le plus observé',
            'Concentration Moyenne',
            'Valeur maximale mesurée',
            'Valeur minimale mesurée',
            'Écart type des données',
            'Nombre total d\'échantillons',
          ]"
          :selected-country="selectedCountry"
        />
      </table>
      <div class="flex flex-row items-center justify-center space-x-4 w-full px-2 py-6">
        <DefaultButton v-for="country in selectedCountry" :label="'Explorez ' + country.name" :to="{ name: 'dashboard', query: { country: country.name }} " />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { RouterLink } from "vue-router"
import type * as types from "@/type"
import CountryTable from "@/components/tables/CountryTable.vue"
import DefaultButton from "@/components/reusable/buttons/DefaultButton.vue"

defineProps<{
  selectedCountry: types.Country[]
  generalInfo: {[key: string]: types.CountryGeneralInfo}
}>()
</script>
