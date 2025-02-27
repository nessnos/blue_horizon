<template>
  <div class="relative group">
    <RouterLink
      :to="to"
      :class="[
        isActive ? 'bg-white' : '',
        'flex flex-row gap-4 rounded-lg p-3 text-white transition duration-200 ease-in-out',
        isActive ? '' : 'transition-all duration-200 ease-in-out hover:cursor-pointer hover:bg-blue-900'
      ]"
    >
      <component :is="icon" :class="['h-6 w-6', isActive ? 'text-ocean' : 'text-white']" />
    </RouterLink>
    <div
      class="absolute left-1/2 transform translate-x-6 -translate-y-10 mt-1 rounded-lg bg-black bg-opacity-80 text-white text-xs px-2 py-1 opacity-0 group-hover:opacity-100 transition-opacity duration-200 pointer-events-none"
    >
      {{ label }}
    </div>
  </div>
</template>

<script lang="ts" setup>

const { to, icon, label, isActive } = defineProps<{
  to: string;
  icon: any;
  label: string;
  isActive: boolean;
}>()
</script>
