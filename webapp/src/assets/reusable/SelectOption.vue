<script setup lang="ts">
  import { ref } from 'vue'
  import { Listbox, ListboxButton, ListboxOptions, ListboxOption,} from '@headlessui/vue';
  import type { Option } from '@/type' ;

  const props = defineProps<{
        rowData: Option[];
        label: String;
    }>();
  const selectedData = ref(props.rowData[0])
</script>

<template>
    <div class="w-72">
      <span class="pl-1 mb-3 text-sm text-ocean font-semibold">{{ label }}</span>
      <Listbox v-model="selectedData">
        <div class="relative mt-1">
          <ListboxButton
            class="relative w-full cursor-default border border-ocean/55 rounded-lg text-sm bg-white py-2 pl-3 pr-10 text-left shadow bg-gray-200/25"
          >
            <span class="block truncate" v-if="selectedData">{{ selectedData.name }}</span>
          </ListboxButton>
  
          <transition
            leave-active-class="transition duration-100 ease-in"
            leave-from-class="opacity-100"
            leave-to-class="opacity-0"
          >
            <ListboxOptions
              class="absolute mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-sm shadow-md"
            >
              <ListboxOption
                v-slot="{ active, selected }"
                v-for="data in rowData"
                :key="data.name"
                :value="data"
                as="template"
              >
                <li
                  :class="[
                    active ? 'bg-ocean text-white' : 'text-gray-900',
                    'relative cursor-default select-none py-2 pl-4 pr-4',
                  ]"
                >
                  <span
                    :class="[
                      selected ? 'font-medium' : 'font-normal',
                      'block truncate',
                    ]"
                    >{{ data.name }}</span
                  >
                  <span
                    v-if="selected"
                    class="absolute inset-y-0 left-0 flex items-center pl-3 text-amber-600"
                  >
                  </span>
                </li>
              </ListboxOption>
            </ListboxOptions>
          </transition>
        </div>
      </Listbox>
    </div>
  </template>
  

  