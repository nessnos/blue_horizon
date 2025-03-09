<template>
    <div class="p-12 py-8 w-full h-full flex flex-col items-start justify-start">
        <div class="flex flex-row gap-3 py-4 items-end">
            <SelectOption v-if="models.length" :rowData="models" :label="'Modèles'" :default="models[0]"
                @update:selectedData="getSelectedModel" />
            <SelectOption v-if="countries.length" :default="countries[0]" :label="'Pays'" :rowData="countries"
                :flag='true' @update:selectedData="filterOptions" />
            <SelectOption v-if="observedProperties.length" :default="observedProperties[0]"
                :label="'Déterminant de propriété observée'" :rowData="observedProperties"
                @update:selectedData="getSelectedObservedProperty" />
            <button
                class="inline-flex justify-center rounded-md border border-transparent bg-ocean px-4 py-2 text-sm font-medium text-white hover:bg-blue-900 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                type="button" @click="runModel">
                Lancer l'algorithme
            </button>
        </div>
        <div class="max-w-full" v-if="selectedModel.parameters && Object.keys(selectedModel.parameters).length">
            <ParameterDisclosure :title="'Paramètres du modèle'" :parameters="selectedModel.parameters" />
        </div>
        <div
            class="relative flex flex-col w-full h-full overflow-scroll text-ocean border border-ocean/50 bg-aqua/10 rounded-lg my-4 p-3">
            <PipelineTable :columns="columns" :data="pipelines" />
        </div>
    </div>
</template>
<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { RouterView, RouterLink, useRoute, useRouter } from "vue-router"

import type * as types from "@/type";
import SelectOption from "@/components/reusable/dropdowns/SelectOption.vue"
import PipelineTable from "@/components/tables/PipelineTable.vue";
import ParameterDisclosure from "@/components/reusable/disclosure/ParameterDisclosure.vue";
import axios from 'axios'

const models = ref<types.Model[]>([
    {
        name: "Régression Linéaire",
        technical_name: "linear-regression",
        parameters: {
            fit_intercept: { value: true, type: "checkbox", label: "Ajuster l'interception" },
        },
    },
    {
        name: "Régression par Forêt Aléatoire",
        technical_name: "rf-regression",
        parameters: {
            n_estimators: { value: 100, type: "slider", min: 10, max: 500, step: 10, label: "Nombre d'estimateurs" },
            max_depth: { value: 1, type: "slider", min: 1, max: 50, step: 1, label: "Profondeur maximale" },
        },
    },
    {
        name: "ARIMA",
        technical_name: "arima",
        parameters: {
            p: { value: 1, type: "slider", min: 0, max: 5, step: 1, label: "Paramètre p (Auto-régressif)" },
            d: { value: 1, type: "slider", min: 0, max: 2, step: 1, label: "Paramètre d (Différenciation)" },
            q: { value: 1, type: "slider", min: 0, max: 5, step: 1, label: "Paramètre q (Moyenne mobile)" },
        },
    }
]);

const countries = ref<types.Option[]>([]);
const observedProperties = ref<types.Option[]>([]);
const pipelines = ref<types.Pipeline[]>([]);

const selectedModel = ref(models.value[0])
const selectedCountry = ref<types.Option>(countries.value[0]);
const selectedObservedProperty = ref<types.Option>(observedProperties.value[0]);

const columns :  {key: keyof types.Pipeline; label?: string}[] = [
  { key: "id", label: "ID" },
  { key: "task_id", label: "Tâche ID" },
  { key: "model_name", label: "Nom du Modèle" },
  { key: "started_at", label: "Commencé à" },
  { key: "completed_at", label: "Complété à" },
  { key: "status", label: "Statut" }
]

const filterOptions = async (payload: types.Option) => {
    selectedCountry.value = payload
    try {
        const response = await axios.post('/api/data/?include_all=false', {
            filter_kwargs: { 'country': selectedCountry.value.name },
            include: ['observedProperties']
        });
        observedProperties.value = response.data.observedProperties
        selectedObservedProperty.value = observedProperties.value[0]
    } catch (error) {
        console.error(error);
    }
}

const getSelectedObservedProperty = (payload: types.Option) => {
    selectedObservedProperty.value = payload
}

const getSelectedModel = (payload: types.Model) => {
    selectedModel.value = payload
}

onMounted(async () => {
    try {
        const response = await axios.post('/api/data/?include_all=false', {
            include: ['observedProperties']
        });
        countries.value = response.data.countries
        observedProperties.value = response.data.observedProperties
        filterOptions(countries.value[0])
    } catch (error) {
        console.error(error);
    }

    await axios.get('/api/data/pipelines/')
        .then(response => {
            pipelines.value = response.data
            console.log(pipelines.value)
        })
        .catch(error => {
            console.log(error)
        })
})

const checkPipelinesStatus = async () => {
    const interval = setInterval(async () => {
        try {
            const response = await axios.get('/api/data/pipelines/');
            pipelines.value = response.data;

            if (pipelines.value.every(pipeline => pipeline.status === "FAILURE" || pipeline.status === "SUCCESS")) {
                clearInterval(interval);
            }
        } catch (error) {
            console.log(error);
            clearInterval(interval);
        }
    }, 2000);
};

const runModel = async () => {
    await axios.post('/api/ml/run/' + selectedModel.value.technical_name, { 'model': selectedModel.value, 'filter_kwargs': { 'countryCode': selectedCountry.value.code, 'observedPropertyDeterminandLabel': selectedObservedProperty.value.name } })
        .then(response => {
            checkPipelinesStatus()
            console.log(response.data)
        })
        .catch(error => {
            console.log(error)
        })
}
</script>