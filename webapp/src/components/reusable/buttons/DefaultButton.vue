<template>
  <div class="group relative">
    <RouterLink
      :to="parsedTo"
      class="rounded-lg bg-ocean px-3 py-2 text-sm text-white transition-all duration-200 ease-in-out hover:bg-gray-100/55 hover:text-ocean hover:outline hover:outline-1 hover:outline-ocean"
    >
      {{ label }}
    </RouterLink>
  </div>
</template>

<script lang="ts" setup>
import { computed } from 'vue'

const props = defineProps<{
  to: string | object
  label: string
}>()

const parsedTo = computed(() => {
  try {
    return typeof props.to === 'string' ? JSON.parse(props.to) : props.to
  } catch (error) {
    return props.to
  }
})
</script>
