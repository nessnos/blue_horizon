<template>
  <div v-if="isLoadingData && !noData" class="flex h-full w-full items-center justify-center">
    <LoadingWheel />
  </div>
  <div v-else class="flex h-full w-full flex-col items-start justify-between gap-2 p-10 py-4">
    <div class="flex flex-row items-center justify-between w-full">
      <SelectOption v-if="countries.length" :default="countries.find((country) => country.name === route.query.country) ||
        countries[0]
        " :label="'Pays'" :rowData="countries" :flag='true' @update:selectedData="filterFilters" />
      <SelectOption v-if="decades.length" :default="decades[0]" :label="'Décennies'" :rowData="decades"
        @update:selectedData="filterData($event, 'reference_year__range')" />
      <SelectOption v-if="observedProperties.length" :default="observedProperties[0]"
        :label="'Déterminant de propriété observée'" :rowData="observedProperties"
        @update:selectedData="filterData($event, 'observed_property_determinand')" />
      <SelectOption v-if="matrix.length" :rowData="matrix" :label="'Matrice analysée'" :default="matrix[0]"
        @update:selectedData="filterData($event, 'matrix')" />
    </div>
    <div class="pt-24 flex items-start justify-center w-full h-full font-normal text-xl text-ocean" v-if="noData">
      Pas de données.
    </div>
    <div class="flex h-full w-full flex-col items-start justify-between gap-2 pt-4" v-else>
      <div class="flex w-full flex-row items-center justify-between gap-2" v-if="dashboardData">
        <DashboardInformationCards :tooltip="'Nombre total de toutes les propriétés observées dans l\'ensemble des données collectées.'" :icon="Chemicals" title="Total des propriétés observées"
          :value="dashboardData?.count_chemicals_monitored.toLocaleString('fr-BE', { maximumFractionDigits: 2, })" />
        <DashboardInformationCards :tooltip="'Nombre total de sites où des données de qualité de l\'eau ont été collectées et surveillées.'" :icon="WebDomain" title="Total des sites surveillés"
          :value="dashboardData?.count_monitoring_sites.toLocaleString('fr-BE', { maximumFractionDigits: 2, })" />
        <DashboardInformationCards :tooltip="'Nombre total d\'échantillons collectés pour l\'analyse de la qualité de l\'eau.'" :icon="Sample" title="Total des échantillons collectés"
          :value="dashboardData?.number_of_collected_samples.toLocaleString('fr-BE', { maximumFractionDigits: 2, })" />
        <DashboardInformationCards :tooltip="'Proportion d\'échantillons dont les résultats ont été validés et confirmés.'" :icon="Proportion" title="Taux d'échantillons confirmés"
          :value="(dashboardData?.proportion_of_confirmed_samples * 100).toLocaleString('fr-BE', { maximumFractionDigits: 2, }) + '%'" />
      </div>
      <div class="flex flex-row items-center gap-4 w-full">
        <div class="h-full min-h-fit rounded-lg border border-ocean/50 bg-white p-2 py-3">
          <div class="flex w-full flex-row items-center gap-4 px-3 py-2 pt-0">
            <div class="text-sm font-semibold text-ocean truncate">
              Aperçu des propriétés observées à travers les sites surveillés
            </div>
            <InformationTooltip text="Vue d'ensemble des propriétés observées sur tous les sites surveillés, classées par ordre croissant selon le nombre total d'observations. Inclut les statistiques moyennes, minimales et maximales." />
          </div>
          <div class="w-full">
            <ObservedPropertyTable :data="dashboardData?.determinand_table" :headers="['Déterminant de propriété observée', 'Total des échantillons collectés' , 'Moyenne', 'Minimum' , 'Maximum', 'Udm']" />
          </div>
        </div>
        <div class="h-full min-h-fit rounded-lg border border-ocean/50 bg-white p-2 py-3">
          <div class="flex w-full flex-row items-center gap-4 px-3 py-2 pt-0">
            <div class="text-sm font-semibold text-ocean truncate">
              Vue d'ensemble des catégories des corps d'eau
            </div>
            <InformationTooltip text="Aperçu des catégories des corps d'eau, classées par ordre croissant selon le nombre total d'observations." />
          </div>

          <div class="max-h-40 w-fit pl-3 overflow-y-scroll">
            <table>
              <thead>
                <tr class="border-b border-gray-200 text-center text-xs">
                  <th class="py-2 px-4 text-ellipsis w-44 max-w-44 whitespace-nowrap overflow-hidden text-ellipsis">Catégorie des corps d'eau</th>
                  <th class="py-2 px-4 text-ellipsis w-44 max-w-44 whitespace-nowrap overflow-hidden text-ellipsis">Total des échantillons collectés</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(category, index) in dashboardData?.waterbody_table" :key="index"
                  class="text-center text-xs">
                  <td class="py-2 px-4 w-50 max-w-50 whitespace-nowrap overflow-hidden text-ellipsis">{{ category.category }}</td>
                  <td class="py-2 px-4 truncate max-w-32 w-32 whitespace-nowrap overflow-hidden text-ellipsis">{{ category.number.toLocaleString('fr-BE', {
                    maximumFractionDigits:
                      2,
                  }) }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="h-40">
          <DonutChart v-if="dashboardData" :data="dashboardData?.loq_donut.data"
            :labels="dashboardData?.loq_donut.labels" />
        </div>
      </div>
      <div class="flex w-full flex-row items-center justify-between gap-8">
        <div class="h-full w-1/2 rounded-lg border border-ocean/50 bg-white p-3 px-6">
          <div class="flex w-full flex-row items-center gap-4 px-3 py-2">
            <div class="text-sm font-semibold text-ocean truncate">
              Valeurs moyennes observées au fil du temps (Déterminant de propriété observée)
            </div>
            <InformationTooltip text="Suivi des valeurs moyennes observées au fil du temps, pour le déterminant sélectionné de propriété observée." />
          </div>
          <div class="relative h-3/4">
            <div v-if="!IsLineChartAvailable"
              class="absolute inset-0 cursor-not-allowed flex justify-center items-center text-white text-xl font-normal z-10">
              <span class="text-ocean bg-aqua/30 px-3 py-2 rounded-lg text-sm">Séléctionnez une propriété pour voir son
                évolution temporelle.</span>
            </div>
            <LineChart v-if="dashboardData && IsLineChartAvailable" :data="dashboardData?.property_line" />
          </div>
        </div>
        <div class="h-fit min-h-64 w-1/2 rounded-lg border border-ocean/50 bg-white p-3 px-6">
          <div class="flex w-full flex-row items-center gap-4 px-3 py-2 pt-0">
            <div class="text-sm font-semibold text-ocean truncate">
              Les déterminants les plus observés
            </div>
            <InformationTooltip text="Classement des déterminants les plus fréquemment observés, ordonnés par le nombre total d'échantillons collectés." />
          </div>
          <BarChart v-if="dashboardData" :data="dashboardData?.property_bar" />
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import axios from 'axios'
import { computed, ref, onMounted } from "vue"
import { useRoute } from "vue-router"
import * as types from "@/type"
import LoadingWheel from "@/components/share/LoadingWheel.vue"
import SelectOption from "@/components/reusable/dropdowns/SelectOption.vue"
import BarChart from "@/components/reusable/charts/BarChart.vue"
import DonutChart from "@/components/reusable/charts/DonutChart.vue"
import LineChart from "@/components/reusable/charts/LineChart.vue"
import Chemicals from "@/assets/icons/Chemicals.vue"
import WebDomain from "@/assets/icons/WebDomain.vue"
import Sample from "@/assets/icons/Sample.vue"
import Proportion from "@/assets/icons/Proportion.vue"
import DashboardInformationCards from "@/components/reusable/cards/DashboardInformationCards.vue"
import InformationTooltip from "@/components/reusable/tooltips/InformationTooltip.vue"
import ObservedPropertyTable from "@/components/tables/ObservedPropertyTable.vue"


const route = useRoute()
const isLoadingData = computed(() => {
  return !dashboardData.value ||
    countries.value.length === 0 ||
    decades.value.length === 0 ||
    observedProperties.value.length === 0 ||
    matrix.value.length === 0;
});

const IsLineChartAvailable = computed(() => {
  return filters.value["observed_property_determinand"] != 'Tout';
});

const noData = ref<boolean>(false)
const countries = ref<types.Option[]>([]);
const decades = ref<types.Option[]>([]);
const observedProperties = ref<types.Option[]>([]);
const matrix = ref<types.Option[]>([]);
const dashboardData = ref<types.DashboardData | null>(null)
const filters = ref<types.FilterType>({ 'country': 'Tout', 'reference_year__range': 'Tout', 'observed_property_determinand': 'Tout', 'matrix': 'Tout' })


onMounted(async () => {
  try {
    if (route?.query.country) {
      const response = await axios.post('/api/data/?include_all=true', {
        filter_kwargs: { 'country': route?.query.country },
        include: ['decades', 'observedProperties', 'matrix']
      });
      countries.value = response.data.countries
      decades.value = response.data.decades
      observedProperties.value = response.data.observedProperties
      matrix.value = response.data.matrix


      filters.value['country'] = (route.query.country as string) ?? 'Tout'
    }
    else {
      const response = await axios.post('/api/data/?include_all=true', {
        include: ['decades', 'observedProperties', 'matrix']
      });
      countries.value = response.data.countries
      decades.value = response.data.decades
      observedProperties.value = response.data.observedProperties
      matrix.value = response.data.matrix
    }
  } catch (error) {
    console.error(error);
  }


  try {
    const response = await axios.post('/api/stats/dashboard/', {
      filter_kwargs: filters.value
    });
    if (response.status === 204) {
      dashboardData.value = null;
      noData.value = true;
    } else {
      dashboardData.value = response.data
      noData.value = false
    }

  } catch (error) {
    console.error(error);
  }
});


const filterFilters = async (payload: types.Option) => {
  try {
    const response = await axios.post('/api/data/?include_all=true', {
      filter_kwargs: { 'country': payload.name },
      include: ['decades', 'observedProperties', 'matrix']
    });
    decades.value = response.data.decades
    observedProperties.value = response.data.observedProperties
    matrix.value = response.data.matrix

    filters.value = { 'country': 'Tout', 'reference_year__range': 'Tout', 'observed_property_determinand': 'Tout', 'matrix': 'Tout' }
  }
  catch (error) {
    console.error(error);
  }

  filters.value['country'] = payload.name
  try {
    const response = await axios.post('/api/stats/dashboard/', {
      filter_kwargs: filters.value
    });
    if (response.status === 204) {
      dashboardData.value = null;
      noData.value = true;
    } else {
      dashboardData.value = response.data
      noData.value = false
    }
  }
  catch (error) {
    console.error(error);
  }
};


const filterData = async (payload: types.Option, filterName: keyof types.FilterType) => {
  if (filterName != 'reference_year__range') {
    filters.value[filterName] = payload.name
  }
  else {
    if (payload.name !== "Tout") {
      if (payload.start && payload.end) {
        filters.value[filterName] = [payload.start, payload.end];
      }
    } else {
      delete filters.value[filterName];
    }
  }

  try {
    const response = await axios.post('/api/stats/dashboard/', {
      filter_kwargs: filters.value
    });
    if (response.status === 204) {
      dashboardData.value = null;
      noData.value = true;
    } else {
      dashboardData.value = response.data
      noData.value = false
    }
  } catch (error) {
    console.error(error);
  }
}
</script>
