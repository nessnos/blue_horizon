<template>
  <Disclosure v-slot="{ open }" :defaultOpen="true">
    <DisclosureButton
      class="flex w-full items-end justify-start gap-4 rounded-lg px-4 py-2 text-left text-sm font-medium text-ocean"
    >
      <span>{{ title }}</span>
      <ChevronUpIcon
        :class="open ? 'rotate-180 transform' : ''"
        class="h-4 w-4 text-ocean"
      />
    </DisclosureButton>

    <DisclosurePanel class="px-4 pb-2 pt-4 text-sm">
      <div
        class="flex flex-row items-center gap-3 px-4"
        v-if="parameters && Object.keys(parameters).length"
      >
        <div
          v-for="(param, key) in parameters"
          :key="key"
          class="flex flex-row items-center gap-3 px-4"
        >
          <label class="block text-xs font-semibold text-ocean">{{
            param.label
          }}</label>

          <input
            v-if="param.type === 'checkbox'"
            type="checkbox"
            v-model="param.value"
            class="h-3 w-3 rounded-sm border-none bg-gray-300 p-1 text-ocean focus:outline-none focus:ring-0 focus:ring-offset-0"
          />

          <input
            v-else-if="param.type === 'slider'"
            type="range"
            v-model="param.value"
            :min="param.min"
            :max="param.max"
            :step="param.step"
            class="w-full cursor-pointer appearance-none bg-transparent"
          />

          <span v-if="param.type !== 'checkbox'" class="text-xs text-ocean">
            {{ param.value }}
          </span>
        </div>
      </div>
      <p v-else class="text-gray-500">
        Aucun paramètre disponible pour ce modèle.
      </p>
    </DisclosurePanel>
  </Disclosure>
</template>

<script setup lang="ts">
import { defineProps } from "vue"
import { Disclosure, DisclosureButton, DisclosurePanel } from "@headlessui/vue"
import { ChevronUpIcon } from "@heroicons/vue/24/outline"

defineProps<{
  title: string
  parameters: Record<
    string,
    {
      label: string
      type: string
      value: any
      min?: number
      max?: number
      step?: number
    }
  >
}>()
</script>

<style scoped>
/* Firefox customization */
input[type="range"]::-moz-range-track {
  background: #d1d5db;
  height: 5px;
  border-radius: 5px;
}

input[type="range"]::-moz-range-thumb {
  background: #002665;
  border-radius: 50%;
  width: 12px;
  height: 12px;
  cursor: pointer;
  border: none;
}

input[type="range"]:disabled {
  pointer-events: none;
  opacity: 0.5;
}

input[type="range"]:disabled::-moz-range-track {
  background: #e0e0e0 !important;
}

input[type="range"]:disabled::-moz-range-thumb {
  background: #b0b0b0 !important;
}
</style>
