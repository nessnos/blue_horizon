<template>
  <div class="flex h-full w-full flex-col items-start justify-start p-12 py-8">
    <div
      v-if="!chatStarted"
      class="mt-28 flex h-full w-full flex-col items-center justify-start gap-2 text-center"
    >
      <div class="mb-4 w-32">
        <img
          alt="Blue Horizon"
          src="@/assets/images/Blue%20Horizon%20Logo.png"
        />
      </div>

      <div class="text-2xl font-semibold text-ocean">
        Bienvenue dans notre chat en démo !
      </div>
      <div class="w-1/3 p-3 text-sm font-normal text-ocean">
        Pour une expérience optimale, merci de sélectionner un pays. Cela nous
        permettra de vous fournir des réponses plus rapides et pertinentes.
        Notez que seules les données à partir de 2020 sont utilisées pour cette
        démo.
      </div>
      <SelectOption
        v-if="countries.length"
        :default="countries[0]"
        :label="''"
        :rowData="countries"
        :flag="true"
        @update:selectedData="getSelectCountry"
      />
      <div class="mt-2">
        <button
          class="inline-flex justify-center rounded-md border border-transparent bg-ocean px-4 py-2 text-sm font-medium text-white hover:bg-blue-900 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
          type="button"
          @click="chatStarted = true"
        >
          Continuer
        </button>
      </div>
    </div>
    <div class="h-4/5 w-full overflow-scroll" v-else>
      <div
        class="flex h-fit w-full flex-col gap-3 px-6"
        v-for="message in history"
      >
        <div
          v-if="message.role.toString() === 'user'"
          class="flex w-full justify-end py-2"
        >
          <div
            class="w-fit max-w-full rounded-lg bg-ocean p-3 text-left text-sm font-normal text-white"
          >
            {{ message.content }}
          </div>
        </div>
        <div
          v-if="message.role.toString() === 'assistant'"
          class="flex justify-start py-2"
        >
          <div
            v-html="message.content"
            class="w-fit max-w-full rounded-lg bg-aqua/30 p-3 text-left text-sm font-normal text-ocean"
          ></div>
        </div>
      </div>
      <div
        v-if="IsGenerating"
        class="animate-pulse px-6 py-2 text-sm text-gray-400"
      >
        Génération de la réponse en cours...
      </div>
      <div
        class="fixed bottom-0 right-0 flex w-full flex-row items-center justify-center gap-3 py-5"
      >
        <div class="flex w-2/3 flex-col items-start justify-center gap-3">
          <div class="flex flex-row items-center gap-3">
            <span
              class="fi rounded-[0.2rem] shadow"
              :class="'fi-' + selectedCountry.code?.toLowerCase()"
            ></span>
            <span class="text-xs font-normal">{{ selectedCountry.name }}</span>
          </div>
          <textarea
            v-model="request"
            rows="1"
            @keyup.enter.prevent="sendRequest"
            class="w-full resize-none rounded-lg border border-gray-300 bg-gray-50 p-2.5 text-sm text-gray-900 focus:border-transparent focus:outline-none focus:outline-none focus-visible:ring-2 focus-visible:ring-ocean"
            placeholder="Ecrivez votre question..."
          ></textarea>
        </div>
        <div class="mt-8">
          <button
            :disabled="IsGenerating"
            class="inline-flex justify-center rounded-md border border-transparent bg-ocean px-4 py-2 text-sm font-medium text-white hover:bg-blue-900 focus:outline-none disabled:cursor-not-allowed"
            type="button"
            @click="sendRequest"
          >
            Envoyer
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue"
import type * as types from "@/type"
import SelectOption from "@/components/reusable/dropdowns/SelectOption.vue"

import axios from "axios"
import { marked } from "marked"

const request = ref<string>("")
const history = ref<types.Message[]>([])
const IsGenerating = ref<boolean>(false)

const chatStarted = ref<boolean>(false)
const countries = ref<types.Option[]>([])
const selectedCountry = ref<types.Option>(countries.value[0])

onMounted(async () => {
  try {
    const response = await axios.get("/api/chat/data/")
    countries.value = response.data
    selectedCountry.value = countries.value[0]
  } catch (error) {
    console.error(error)
  }
})

const getSelectCountry = (payload: types.Option) => {
  selectedCountry.value = payload
}

const sendRequest = async () => {
  history.value.push({ role: "user", content: request.value })
  request.value = ""
  IsGenerating.value = true
  await axios
    .post("/api/chat/answer/", {
      history: history.value,
      country: selectedCountry.value,
    })
    .then((response) => {
      IsGenerating.value = false
      var answer = marked.parse(response.data.message)
      history.value.push({ role: "assistant", content: answer })
      console.log(history.value)
    })
    .catch((error) => {
      console.log(error)
    })
}
</script>
