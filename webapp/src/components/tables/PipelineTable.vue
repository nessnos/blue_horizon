<template>
  <div class="w-full max-w-full overflow-x-auto">
    <table class="w-full table-fixed border-collapse">
      <thead>
        <tr>
          <th
            v-for="col in columns"
            :key="col.key"
            :class="[
              data.some((pipeline) => pipeline.status === 'SUCCESS')
                ? 'w-1/' + columns.length
                : 'w-1/' + (columns.length - 2),
            ]"
            class="border-blue-gray-100 bg-blue-gray-50 truncate border-b p-4 text-center text-sm font-normal text-ocean opacity-70"
          >
            {{ col.label }}
          </th>
          <th
            v-if="data.some((pipeline) => pipeline.status === 'SUCCESS')"
            :class="'w-1/' + columns.length"
            class="border-blue-gray-100 border-b p-4"
          ></th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="data.length" v-for="pipeline in data" :key="pipeline.id">
          <td
            v-for="(column, index) in columns"
            :key="index"
            :class="[
              data.some((pipeline) => pipeline.status === 'SUCCESS')
                ? 'w-1/' + columns.length
                : 'w-1/' + (columns.length - 2),
            ]"
            class="border-blue-gray-50 border-b p-4"
          >
            <div
              class="block truncate text-center font-sans text-sm font-normal leading-normal antialiased"
            >
              <span
                v-if="
                  column.key == 'completed_at' || column.key == 'started_at'
                "
              >
                {{
                  moment(String(pipeline?.completed_at)).format(
                    "DD/MM/YYYY HH:mm:ss"
                  )
                }}
              </span>
              <span
                v-else
                :class="[
                  column.key === 'status'
                    ? getStatusClass(pipeline[column.key])
                    : 'text-ocean',
                ]"
                >{{ pipeline[column.key] }}</span
              >
            </div>
          </td>
          <td
            class="border-blue-gray-50 border-b p-4"
            :class="'w-1/' + columns.length"
          >
            <RouterLink
              v-if="pipeline.status === 'SUCCESS'"
              :to="{
                path: '/machine-learning/details/pipeline',
                query: { id: pipeline.id },
              }"
              class="text-sm font-semibold text-ocean underline"
            >
              Voir Résultats
            </RouterLink>
          </td>
        </tr>
        <tr v-else>
          <td
            :colspan="columns.length + 1"
            class="p-4 text-center text-sm font-normal text-ocean"
          >
            Pas de données trouvées.
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script lang="ts" setup>
import moment from "moment"
import type * as types from "@/type"

defineProps<{
  columns: { key: keyof types.Pipeline; label?: string }[]
  data: types.Pipeline[]
}>()

const getStatusClass = (status: string) => {
  let classGroup = "my-2 p-2 text-xs rounded-lg font-semibold"
  switch (status) {
    case "PENDING":
      return classGroup + " text-yellow-500 bg-yellow-100"
    case "STARTED":
      return classGroup + " text-blue-500 bg-blue-100"
    case "SUCCESS":
      return classGroup + " text-green-500 bg-green-100"
    case "FAILURE":
      return classGroup + " text-red-500 bg-red-100"
    default:
      return classGroup + " text-gray-500 bg-gray-100"
  }
}
</script>
