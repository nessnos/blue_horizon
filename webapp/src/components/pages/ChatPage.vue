<template>
  <div class="p-12 py-8 w-full h-full flex flex-col items-start justify-start">
    <div v-if="!chatStarted" class="flex flex-col items-center justify-start gap-2 mt-28 text-center w-full h-full">
      <div class="mb-4 w-32">
        <img alt="Blue Horizon" src="@/assets/images/Blue%20Horizon%20Logo.png" />
      </div>

      <div class="font-semibold text-ocean text-2xl">
        Bienvenue dans notre chat en démo !
      </div>
      <div class="text-sm font-normal p-3 w-1/3 text-ocean">
        Pour une expérience optimale, merci de sélectionner un pays. Cela nous permettra de vous fournir des réponses
        plus rapides et pertinentes. Notez que seules les données à partir de 2020 sont utilisées pour cette démo.
      </div>
      <SelectOption v-if="countries.length" :default="countries[0]
        " :label="''" :rowData="countries" :flag='true' @update:selectedData="getSelectCountry" />
      <div class="mt-2">
        <button
          class="inline-flex justify-center rounded-md border border-transparent bg-ocean px-4 py-2 text-sm font-medium text-white hover:bg-blue-900 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
          type="button" @click="chatStarted = true
            ">
          Continuer
        </button>
      </div>
    </div>
    <div class="w-full h-4/5 overflow-scroll" v-else>
      <div class="px-6 h-fit w-full flex flex-col gap-3" v-for="message in history">
        <div v-if="message.role.toString() === 'user'" class="flex justify-end py-2 w-full">
          <div class="bg-ocean rounded-lg p-3 text-white text-sm font-normal text-left w-fit max-w-full">
            {{ message.content }}
          </div>
        </div>
        <div v-if="message.role.toString() === 'assistant'" class="flex justify-start py-2">
          <div v-html="message.content"
            class="text-ocean bg-aqua/30 rounded-lg p-3 text-sm font-normal text-left w-fit max-w-full">
          </div>
        </div>
      </div>
      <div v-if="IsGenerating" class="px-6 py-2 text-sm text-gray-400 animate-pulse">
        Génération de la réponse en cours...
      </div>
      <div class="fixed bottom-0 right-0 py-5 flex flex-row items-center justify-center gap-3 w-full">
        <div class="flex flex-col gap-3 items-start justify-center w-2/3">
          <div class="flex flex-row gap-3 items-center">
            <span class="fi rounded-[0.2rem] shadow" :class="'fi-' + selectedCountry.code?.toLowerCase()"></span>
            <span class="font-normal text-xs">{{ selectedCountry.name }}</span>
          </div>
          <textarea v-model="request" rows="4"
            class="w-full resize-none p-2.5 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:outline-none focus:border-transparent focus:outline-none focus-visible:ring-2 focus-visible:ring-ocean"
            placeholder="Ecrivez votre question..."></textarea>

        </div>
        <div class="mt-8">
          <button :disabled="IsGenerating"
            class="disabled:cursor-not-allowed inline-flex justify-center rounded-md border border-transparent bg-ocean px-4 py-2 text-sm font-medium text-white hover:bg-blue-900 focus:outline-none"
            type="button" @click="sendRequest">
            Envoyer
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import type * as types from "@/type";
import SelectOption from "@/components/reusable/dropdowns/SelectOption.vue"
import DefaultButton from "@/components/reusable/buttons/DefaultButton.vue"

import axios from 'axios';
import { marked } from 'marked';

const request = ref<string>('')
const history = ref<types.Message[]>([])
const IsGenerating = ref<boolean>(false)

const chatStarted = ref<boolean>(false)
const countries = ref<types.Option[]>([]);
const selectedCountry = ref<types.Option>(countries.value[0])

onMounted(async () => {
  try {
    const response = await axios.get('/api/chat/data/');
    countries.value = response.data
    selectedCountry.value = countries.value[0]
  } catch (error) {
    console.error(error);
  }
})

const getSelectCountry = (payload: types.Option) => {
  selectedCountry.value = payload
}

const sendRequest = async () => {
  history.value.push({ 'role': 'user', 'content': request.value })
  request.value = ''
  IsGenerating.value = true
  await axios.post('/api/chat/answer/',
    { 'history': history.value, 'country': selectedCountry.value })
    .then(response => {
      IsGenerating.value = false
      var answer = marked.parse(response.data.message)
      history.value.push({ 'role': 'assistant', 'content': answer })
      console.log(history.value)
    })
    .catch(error => {
      console.log(error)
    })
};
</script>