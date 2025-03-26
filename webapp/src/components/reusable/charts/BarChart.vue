<template>
  <div id="bar-chart" class="px-2 pt-4"></div>
</template>
<script lang="ts" setup>
import { onMounted, ref, watch } from "vue"
import ApexCharts from "apexcharts"
import type * as types from "@/type"

const props = defineProps<{
  data: types.ChartData[] | undefined
}>()

const categories = ref<(string | string[])[]>([])

const splitCategories = () => {
  if (props?.data) {
    categories.value = props.data.map((element) => {
      return element.x.toString().split(" ")
    })
  }
}

let chart: ApexCharts | null = null

const renderChart = () => {
  const options = {
    series: [
      {
        name: "Chemicals",
        color: "#002665",
        data: props.data,
      },
    ],
    states: {
      active: {
        filter: {
          type: "none",
        },
      },
    },
    chart: {
      type: "bar",
      height: "100%",
      width: "100%",
      fontFamily: "Inter, sans-serif",
      toolbar: {
        show: false,
      },
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: "85%",
        borderRadiusApplication: "end",
        borderRadius: 4,
        dataLabels: {
          position: "top",
        },
        value: {
          formatter: (value: string) =>
            parseInt(value)
              .toLocaleString("fr-BE", { maximumFractionDigits: 2 })
              .toString(),
        },
      },
    },
    tooltip: {
      enabled: true,
      custom: function ({
        series,
        seriesIndex,
        dataPointIndex,
        w,
      }: {
        series: number[][]
        seriesIndex: number
        dataPointIndex: number
        w: any
      }) {
        const dataPoint = series[seriesIndex][dataPointIndex]
        const category = w.globals.labels[dataPointIndex]
        return `<div class="p-[5px] bg-black/80 text-white text-xs border-none;">
                  ${category} : ${dataPoint.toLocaleString("fr-BE", {
          maximumFractionDigits: 2,
        })}
                </div>`
      },
    },

    grid: {
      show: false,
      strokeDashArray: 4,
      padding: {
        left: 6,
        right: 6,
        top: 0,
      },
    },
    dataLabels: {
      enabled: true,
      offsetY: -25,
      style: {
        fontSize: "12px",
        colors: ["#002665"],
        fontWeight: "400",
      },
      formatter: function (value: number) {
        return value.toLocaleString("fr-BE", { maximumFractionDigits: 2 })
      },
    },
    legend: {
      show: false,
      position: "right",
    },
    xaxis: {
      categories: categories.value,
      floating: false,
      labels: {
        rotate: 0,
        show: true,
        style: {
          cssClass: "text-xs font-semibold fill-ocean truncate",
        },
        maxWidth: 20,
      },
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
    },
    yaxis: {
      show: false,
    },
    fill: {
      opacity: 1,
    },
  }

  if (chart) {
    chart.destroy()
  }

  chart = new ApexCharts(document.getElementById("bar-chart"), options)
  chart.render()
}

onMounted(() => {
  renderChart()
  splitCategories()
})

watch(
  () => props.data,
  () => {
    splitCategories()
    renderChart()
  },
  { deep: true }
)
</script>
