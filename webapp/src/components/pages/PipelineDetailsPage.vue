<template>
    <div v-if="pipeline" class="p-12 py-8 w-full h-full flex flex-col gap-4 items-center justify-start">
        <div class="flex flex-row gap-4 items-center justify-center w-full h-1/2">
            <div class="rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4 w-1/2 h-full overflow-y-scroll">
                <div class="flex flex-col gap-6 justify-start items-start h-full">
                    <div class="font-semibold text-sm text-ocean">Résultats de l'algorithme</div>
                    <table>
                        <thead>
                            <tr class="border-b border-gray-200 text-center text-xs">
                                <th class="py-2 px-4">Année</th>
                                <th class="py-2 px-4">Prédictions futures</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="(pred, index) in pipeline?.results.series[pipeline.results.series.length - 1]?.data" :key="index"
                                class="text-center text-xs">
                                <td class="py-2 px-4 w-96">{{ pred.x }}</td>
                                <td class="py-2 px-4 w-96">{{ pred.y.toLocaleString('fr-BE', {
                                    maximumFractionDigits:
                                        2,
                                    }) }}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
            <div class="rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4 w-1/2 h-full">
                <div class="flex flex-col gap-3 justify-start items-start h-full">
                    <div class="font-semibold text-sm text-ocean">Paramètres</div>
                    <div class="px-2 flex flex-row w-full justify-between">
                        <div class="text-xs font-normal text-gray-500">Pays</div>
                        <div class="text-xs text-ocean">{{ pipeline?.results.country }}</div>
                    </div>
                    <div class="px-2 flex flex-row w-full justify-between">
                        <div class="text-xs font-normal text-gray-500">Déterminant de propriété observée</div>
                        <div class="text-xs text-ocean">{{ pipeline?.results.observedProperty }}</div>
                    </div>
                    <div class="px-2 flex flex-row w-full justify-between"
                        v-for="(param, key) in pipeline?.results.parameters">
                        <div class="text-xs font-normal text-gray-500">{{ param['label'] }}</div>
                        <div class="text-xs text-ocean">{{ param['value'] }}</div>
                    </div>
                    <div class="font-semibold text-sm text-ocean">Détails du modèle</div>
                    <div class="px-2 flex flex-row w-full justify-between">
                        <div class="text-xs font-normal text-gray-500">Nom du Modèle</div>
                        <div class="text-xs text-ocean">{{ pipeline?.model_name }}</div>
                    </div>
                    <div class="px-2 flex flex-row w-full justify-between">
                        <div class="text-xs font-normal text-gray-500">Commencé à</div>
                        <div class="text-xs text-ocean">{{ moment(String(pipeline?.started_at)).format('DD/MM/YYYYHH:mm:ss') }}
                        </div>
                    </div>
                    <div class="px-2 flex flex-row w-full justify-between">
                        <div class="text-xs font-normal text-gray-500">Complété à</div>
                        <div class="text-xs text-ocean">{{ moment(String(pipeline?.completed_at)).format('DD/MM/YYYY HH:mm:ss') }}
                        </div>
                    </div>
                    <div class="px-2 flex flex-row w-full justify-between">
                        <div class="text-xs font-normal text-gray-500">Statut</div>
                        <div class="text-xs text-ocean">{{ pipeline?.status }}</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="flex flex-row gap-4 items-center justify-start w-full h-1/2">
            <div
                class="rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4 flex flex-col gap-2 justify-start items-start w-2/3 h-full">
                <div class="font-semibold text-sm text-ocean">Prédictions du modèle</div>
                <div class="w-full h-[90%]">
                    <ScatterPlot :dataSeries='pipeline.results.series' />
                </div>
            </div>
            <div class="rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4 gap-4 flex flex-col w-1/3 h-full">
                <div class="font-semibold text-sm text-ocean">Performance du modèle</div>
                <div v-if="pipeline?.results" class="flex flex-col gap-3 justify-start items-start w-full">
                    <div v-if="pipeline?.results.metrics.r_squared" class="px-2 flex flex-row w-full justify-between">
                        <div class="text-xs font-normal text-gray-500">R²</div>
                        <div class="text-xs text-ocean">{{ (Number(pipeline?.results.metrics.r_squared) *
                            100).toFixed(2) }}%</div>
                    </div>
                    <div class="px-2 flex flex-row w-full justify-between">
                        <div class="text-xs font-normal text-gray-500">Erreur quadratique moyenne (MSE)</div>
                        <div class="text-xs text-ocean">{{
                            (Number(pipeline?.results.metrics.mean_squared_error)).toFixed(2) }}</div>
                    </div>
                    <div class="px-2 flex flex-row w-full justify-between">
                        <div class="text-xs font-normal text-gray-500">Erreur moyenne absolue (MAE)</div>
                        <div class="text-xs text-ocean">{{
                            (Number(pipeline?.results.metrics.mean_absolute_error)).toFixed(2) }}
                        </div>
                    </div>
                    <div class="px-2 flex flex-row w-full justify-between">
                        <div class="text-xs font-normal text-gray-500">Racine de l'Erreur quadratique moyenne (RMSE)
                        </div>
                        <div class="text-xs text-ocean">{{
                            (Number(pipeline?.results.metrics.root_mean_squared_error)).toFixed(2) }}
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { RouterView, RouterLink, useRoute, useRouter } from "vue-router"
import moment from 'moment';
import type * as types from "@/type";
import ScatterPlot from '@/components/reusable/charts/ScatterPlot.vue';

import axios from 'axios';

const pipeline = ref<types.Pipeline>();
const route = useRoute();

onMounted(async () => {
    await axios.get('/api/data/get-pipeline/?id=' + route.query.id)
        .then(response => {
            pipeline.value = response.data
            console.log(response.data)
        })
        .catch(error => {
            console.log(error)
        })
})
</script>