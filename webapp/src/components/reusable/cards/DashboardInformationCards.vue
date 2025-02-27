<template>
  <div class="h-30 w-fit rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4 text-ocean">
    <div class="flex flex-col items-start gap-8">
      <div class="flex w-full flex-row items-center justify-between">
        <component
          :is="icon"
          class="size-8 text-ocean"
        />
        <div class="text-2xl font-bold">{{ value }}</div>
      </div>
      <div class="flex w-full flex-row justify-between">
        <div class="text-xs font-normal">{{ title }}</div>
        <div class="group relative pl-4">
          <InformationCircleIcon class="h-4 w-4 cursor-pointer text-ocean" />

          <!-- Tooltip -->
          <div
            class="translate-x-1/5 absolute right-0 top-6 z-10 hidden w-fit min-w-32 max-w-56 rounded-md bg-black/80 px-2 py-1 text-center text-[0.7rem] text-white opacity-0 shadow-md transition-opacity duration-200 group-hover:block group-hover:opacity-100"
          >
            More info about collected samples
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { defineProps } from "vue"
import { InformationCircleIcon } from "@heroicons/vue/24/outline"

defineProps<{
  title: string
  value: string | number
  icon: any
}>()
</script>
