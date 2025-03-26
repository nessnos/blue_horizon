<template>
  <div
    v-if="pipeline"
    class="flex h-full w-full flex-col items-center justify-start gap-4 p-12 py-8"
  >
    <div class="flex h-1/2 w-full flex-row items-center justify-center gap-4">
      <div
        class="h-full w-1/2 overflow-y-scroll rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4"
      >
        <div class="flex h-full flex-col items-start justify-start gap-6">
          <div class="text-sm font-semibold text-ocean">
            Résultats de l'algorithme
          </div>
          <table>
            <thead>
              <tr class="border-b border-gray-200 text-center text-xs">
                <th class="px-4 py-2">Année</th>
                <th class="px-4 py-2">Prédictions futures</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="(pred, index) in pipeline?.results.series[
                  pipeline.results.series.length - 1
                ]?.data"
                :key="index"
                class="text-center text-xs"
              >
                <td class="w-96 px-4 py-2">{{ pred.x }}</td>
                <td class="w-96 px-4 py-2">
                  {{
                    pred.y.toLocaleString("fr-BE", {
                      maximumFractionDigits: 2,
                    })
                  }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div
        class="h-full w-1/2 rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4"
      >
        <div class="flex h-full flex-col items-start justify-start gap-3">
          <div class="text-sm font-semibold text-ocean">Paramètres</div>
          <div class="flex w-full flex-row justify-between px-2">
            <div class="text-xs font-normal text-gray-500">Pays</div>
            <div class="text-xs text-ocean">
              {{ pipeline?.results.country }}
            </div>
          </div>
          <div class="flex w-full flex-row justify-between px-2">
            <div class="text-xs font-normal text-gray-500">
              Déterminant de propriété observée
            </div>
            <div class="text-xs text-ocean">
              {{ pipeline?.results.observedProperty }}
            </div>
          </div>
          <div
            class="flex w-full flex-row justify-between px-2"
            v-for="(param, key) in pipeline?.results.parameters"
          >
            <div class="text-xs font-normal text-gray-500">
              {{ param["label"] }}
            </div>
            <div class="text-xs text-ocean">{{ param["value"] }}</div>
          </div>
          <div class="text-sm font-semibold text-ocean">Détails du modèle</div>
          <div class="flex w-full flex-row justify-between px-2">
            <div class="text-xs font-normal text-gray-500">Nom du Modèle</div>
            <div class="text-xs text-ocean">{{ pipeline?.model_name }}</div>
          </div>
          <div class="flex w-full flex-row justify-between px-2">
            <div class="text-xs font-normal text-gray-500">Commencé à</div>
            <div class="text-xs text-ocean">
              {{
                moment(String(pipeline?.started_at)).format(
                  "DD/MM/YYYYHH:mm:ss"
                )
              }}
            </div>
          </div>
          <div class="flex w-full flex-row justify-between px-2">
            <div class="text-xs font-normal text-gray-500">Complété à</div>
            <div class="text-xs text-ocean">
              {{
                moment(String(pipeline?.completed_at)).format(
                  "DD/MM/YYYY HH:mm:ss"
                )
              }}
            </div>
          </div>
          <div class="flex w-full flex-row justify-between px-2">
            <div class="text-xs font-normal text-gray-500">Statut</div>
            <div class="text-xs text-ocean">{{ pipeline?.status }}</div>
          </div>
        </div>
      </div>
    </div>

    <div class="flex h-1/2 w-full flex-row items-center justify-start gap-4">
      <div
        class="flex h-full w-2/3 flex-col items-start justify-start gap-2 rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4"
      >
        <div class="text-sm font-semibold text-ocean">
          Prédictions du modèle
        </div>
        <div class="h-[90%] w-full">
          <ScatterPlot :dataSeries="pipeline.results.series" />
        </div>
      </div>
      <div
        class="flex h-full w-1/3 flex-col gap-4 rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4"
      >
        <div class="text-sm font-semibold text-ocean">
          Performance du modèle
        </div>
        <div
          v-if="pipeline?.results"
          class="flex w-full flex-col items-start justify-start gap-3"
        >
          <div
            v-if="pipeline?.results.metrics.r_squared"
            class="flex w-full flex-row justify-between px-2"
          >
            <div class="text-xs font-normal text-gray-500">R²</div>
            <div class="text-xs text-ocean">
              {{
                (Number(pipeline?.results.metrics.r_squared) * 100).toFixed(2)
              }}%
            </div>
          </div>
          <div class="flex w-full flex-row justify-between px-2">
            <div class="text-xs font-normal text-gray-500">
              Erreur quadratique moyenne (MSE)
            </div>
            <div class="text-xs text-ocean">
              {{
                Number(pipeline?.results.metrics.mean_squared_error).toFixed(2)
              }}
            </div>
          </div>
          <div class="flex w-full flex-row justify-between px-2">
            <div class="text-xs font-normal text-gray-500">
              Erreur moyenne absolue (MAE)
            </div>
            <div class="text-xs text-ocean">
              {{
                Number(pipeline?.results.metrics.mean_absolute_error).toFixed(2)
              }}
            </div>
          </div>
          <div class="flex w-full flex-row justify-between px-2">
            <div class="text-xs font-normal text-gray-500">
              Racine de l'Erreur quadratique moyenne (RMSE)
            </div>
            <div class="text-xs text-ocean">
              {{
                Number(
                  pipeline?.results.metrics.root_mean_squared_error
                ).toFixed(2)
              }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue"
import { useRoute } from "vue-router"
import moment from "moment"
import type * as types from "@/type"
import ScatterPlot from "@/components/reusable/charts/ScatterPlot.vue"

import axios from "axios"

const pipeline = ref<types.Pipeline>()
const route = useRoute()

onMounted(async () => {
  await axios
    .get("/api/data/get-pipeline/?id=" + route.query.id)
    .then((response) => {
      pipeline.value = response.data
      console.log(response.data)
    })
    .catch((error) => {
      console.log(error)
    })
})
</script>
