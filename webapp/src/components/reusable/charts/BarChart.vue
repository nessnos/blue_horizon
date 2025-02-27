<template>
  <div id="bar-chart" class="px-2 pt-4"></div>
</template>
<script lang="ts" setup>
import { onMounted } from "vue"
import ApexCharts from "apexcharts"
import type { BarData } from "@/type"

const props = defineProps<{
  chartData: BarData[]
}>()

onMounted(() => {
  const sortedData = [...props.chartData].sort((a, b) => b.y - a.y)
  const options = {
    series: [
      {
        name: "Chemicals",
        color: "#002665",
        data: sortedData,
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
        columnWidth: "90%",
        borderRadiusApplication: "end",
        borderRadius: 4,
      },
    },
    tooltip: {
      enabled: true,
      custom: function ({ series, seriesIndex, dataPointIndex, w }) {
        const dataPoint = series[seriesIndex][dataPointIndex]
        const category = w.globals.labels[dataPointIndex]
        return `<div class="p-[5px] bg-black/80 text-white text-xs border-none;">
                  ${category}: ${dataPoint}
                </div>`
      },
    },
    grid: {
      show: true,
      strokeDashArray: 4,
      padding: {
        left: 6,
        right: 6,
        top: 0,
      },
    },
    dataLabels: {
      enabled: false,
    },
    legend: {
      show: false,
      position: "right",
    },
    xaxis: {
      floating: false,
      labels: {
        show: true,
        style: {
          cssClass: "text-xs font-normal fill-ocean",
        },
      },
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: false,
      },
    },
    yaxis: {
      show: true,
      tickAmount: "dataPoints",
    },
    fill: {
      opacity: 1,
    },
  }

  if (
    document.getElementById("bar-chart") &&
    typeof ApexCharts !== "undefined"
  ) {
    const chart = new ApexCharts(document.getElementById("bar-chart"), options)
    chart.render()
  }
})
</script>
<style></style>
