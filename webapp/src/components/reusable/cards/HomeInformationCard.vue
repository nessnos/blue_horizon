<template>
  <div
    class="flex h-80 w-64 flex-col items-start justify-between gap-2 rounded-lg border border-ocean/50 bg-aqua/10 px-6 py-4"
  >
    <div class="relative h-full w-full p-1 flex flex-col items-center">
      <component :is="icon" class="text-ocean size-20" />
    </div>
    <div class="py-3">
      <div class="text-sm font-normal">{{ title }}</div>
      <div class="py-2 text-xs">{{ description }}</div>
    </div>
    <DefaultButton
      :label="'Learn More'"
      :to="link"
      />
  </div>
</template>

<script lang="ts" setup>
import DefaultButton from "@/components/reusable/buttons/DefaultButton.vue"

const { title, description, icon, link } = defineProps<{
  title: string
  description: string
  icon: any
  link: string
}>()
</script>
