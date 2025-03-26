<template>
  <div
    class="flex h-96 w-64 flex-col items-start justify-between gap-2 rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4"
  >
    <div class="relative flex h-full w-full flex-col items-center p-1">
      <div
        v-if="demo"
        class="absolute left-[55%] top-0 rounded-full bg-aqua p-1 px-1.5 text-xs font-normal text-ocean"
      >
        demo
      </div>
      <component :is="icon" class="size-20 text-ocean" />
    </div>
    <div class="h-2/3 py-3 align-top text-ocean">
      <div class="text-sm font-semibold">{{ title }}</div>
      <div class="py-2 text-xs">{{ description }}</div>
    </div>
    <DefaultButton :label="'En savoir plus'" :to="link" />
  </div>
</template>

<script lang="ts" setup>
import DefaultButton from "@/components/reusable/buttons/DefaultButton.vue"

const {
  title,
  description,
  icon,
  link,
  demo = false,
} = defineProps<{
  title: string
  description: string
  icon: any
  link: string
  demo?: boolean
}>()
</script>
