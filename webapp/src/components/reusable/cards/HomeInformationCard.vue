<template>
  <div
    class="flex h-80 w-64 flex-col items-start justify-between gap-2 rounded-lg border-[0.5px] border-gray-300 bg-gray-100/55 px-6 py-4 shadow"
  >
    <div class="relative h-40 w-full p-1">
      <img :src="image" alt="" class="h-full w-full rounded object-cover" />
      <div class="absolute bottom-0 h-12 w-full bg-gray-100 blur-lg"></div>
    </div>
    <div class="py-3">
      <div class="text-sm font-normal">{{ title }}</div>
      <div class="py-2 text-xs">{{ description }}</div>
    </div>
    <RouterLink
      :to="link"
      class="rounded-lg bg-ocean px-3 py-2 text-sm text-white transition-all duration-200 ease-in-out hover:bg-gray-100/55 hover:text-ocean hover:outline hover:outline-1 hover:outline-ocean"
    >
      Learn More
    </RouterLink>
  </div>
</template>

<script lang="ts" setup>

const { title, description, image, link } = defineProps<{
  title: string
  description: string
  image: string
  link: string
}>()
</script>
