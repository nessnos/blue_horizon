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
        <InformationTooltip class="pl-4" text="More info about collected samples"/>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { defineProps } from "vue"
import InformationTooltip from "@/components/reusable/tooltips/InformationTooltip.vue";

defineProps<{
  title: string
  value: string | number
  icon: any
}>()
</script>
