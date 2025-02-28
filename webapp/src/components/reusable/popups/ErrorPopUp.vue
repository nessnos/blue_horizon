<template>
<Dialog as="div" class="relative z-10" @close="rightAction">
      <TransitionChild
        as="template"
        enter="duration-300 ease-out"
        enter-from="opacity-0"
        enter-to="opacity-100"
        leave="duration-200 ease-in"
        leave-from="opacity-100"
        leave-to="opacity-0"
      >
        <div class="fixed inset-0 bg-black/25" />
      </TransitionChild>

      <div class="fixed inset-0 overflow-y-auto">
        <div
          class="flex min-h-full items-center justify-center p-4 text-center"
        >
          <TransitionChild
            as="template"
            enter="duration-300 ease-out"
            enter-from="opacity-0 scale-95"
            enter-to="opacity-100 scale-100"
            leave="duration-200 ease-in"
            leave-from="opacity-100 scale-100"
            leave-to="opacity-0 scale-95"
          >
            <DialogPanel
              class="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow  transition-all"
            >
              <DialogTitle
                as="h3"
                class="flex flex-row items-center gap-2 text-lg font-medium leading-6 text-red-700"
              >
                <ExclamationCircleIcon class="h-6 w-6" />
                <span>{{ title }}</span>
              </DialogTitle>
              <div class="mt-6">
                <div class="text-sm text-gray-500">
                  {{ message }}
                </div>
              </div>

              <div class="mt-8 flex flex-row items-center justify-between">
                <button
                  class="inline-flex justify-center rounded-md border border-transparent bg-red-700 px-4 py-2 text-sm font-medium text-white hover:bg-red-600 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                  type="button"
                  @click="leftAction"
                >
                  {{ leftLabel }}
                </button>
                <button
                  class="inline-flex justify-center rounded-md border border-transparent bg-ocean px-4 py-2 text-sm font-medium text-white hover:bg-blue-900 focus:outline-none focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2"
                  type="button"
                  @click="rightAction"
                >
                  {{ rightLabel }}
                </button>
              </div>
            </DialogPanel>
          </TransitionChild>
        </div>
      </div>
    </Dialog>
</template>

<script setup lang="ts">
import {Dialog, DialogPanel, DialogTitle, TransitionChild} from "@headlessui/vue";
import {ExclamationCircleIcon} from "@heroicons/vue/24/solid";
import { defineProps } from "vue"

defineProps<{
  title: string
  message: string
  leftLabel: string
  rightLabel: string
  leftAction: any
  rightAction: any
}>()
</script>