<template>
  <div
    class="flex h-96 w-64 flex-col items-start justify-between gap-2 rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4">
    <div class="relative h-full w-full p-1 flex flex-col items-center">
      <div v-if="demo"
        class="bg-aqua text-ocean p-1 px-1.5 top-0 left-[55%] absolute rounded-full text-xs font-normal">
        demo
      </div>
      <component :is="icon" class="text-ocean size-20" />
    </div>
    <div class="py-3 h-2/3 align-top text-ocean">
      <div class="text-sm font-semibold">{{ title }}</div>
      <div class="py-2 text-xs">{{ description }}</div>
    </div>
    <DefaultButton :label="'En savoir plus'" :to="link" />
  </div>
</template>

<script lang="ts" setup>
import DefaultButton from "@/components/reusable/buttons/DefaultButton.vue"

const { title, description, icon, link, demo = false } = defineProps<{
  title: string
  description: string
  icon: any
  link: string
  demo?: boolean
}>()
</script>
