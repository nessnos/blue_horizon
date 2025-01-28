<template>
      <div class="px-2 pt-4" id="bar-chart"></div>
      </template>
      <script setup lang="ts">
      import { onMounted } from 'vue';
      import ApexCharts from 'apexcharts'
      import type { BarData } from '@/type' ;
      
      const props = defineProps<{
        chartData: BarData[];
        }>();

      onMounted(() => {
      
       const options = {
       //colors: ["#1A56DB", "#FDBA8C"],
       series: [
        {
         name: "MOCs",
         color: "rgba(134, 239, 172,0.75)",
         data: props.chartData,
        },
       ],
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
         columnWidth: "92%",
         borderRadiusApplication: "end",
         borderRadius: 6,
        },
       },
       tooltip: {
        shared: true,
        intersect: false,
        style: {
         fontFamily: "Inter, sans-serif",
        },
       },
       states: {
        hover: {
         filter: {
          type: "darken",
          value: 1,
         },
        },
       },
       stroke: {
        show: true,
        width: 0,
        colors: ["transparent"],
       },
       grid: {
        show: false,
        strokeDashArray: 4,
        padding: {
         left: 1,
         right: 1,
         top: -14
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
          fontFamily: "Inter, sans-serif",
          cssClass: 'text-xs font-normal fill-gray-500'
         }
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
        tickAmount: 5,
       },
       fill: {
        opacity: 1,
       }
      }
      
      if(document.getElementById("bar-chart") && typeof ApexCharts !== 'undefined') {
       const chart = new ApexCharts(document.getElementById("bar-chart"), options);
       chart.render();
      }
      
      })
      </script>
    