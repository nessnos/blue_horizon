<template>
  <RouterLink
    :to="to"
    :class="[
      isActive ? 'bg-white' : '',
      'flex flex-row gap-4 rounded-lg p-3 text-white transition duration-200 ease-in-out',
      isActive ? '' : 'hover:cursor-pointer hover:bg-blue-300 hover:bg-opacity-20'
    ]"
  >
    <component :is="icon" :class="['h-6 w-6', isActive ? 'text-ocean' : 'text-white']" />
  </RouterLink>
</template>

<script lang="ts" setup>
import { defineProps } from 'vue'

const { to, icon, isActive } = defineProps<{
  to: string;
  icon: any;
  isActive: boolean;
}>()
</script>