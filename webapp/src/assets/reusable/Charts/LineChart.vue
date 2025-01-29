<template>
    <div class="px-2 pt-4" id="line-chart"></div>
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
          series: [{
          name: 'Average Chemicals',
          data: [4, 3, 10, 9, 29, 19, 22, 9, 12, 7, 19, 5, 13, 9, 17, 2, 7, 5]
        }],
          chart: {
          height: "100%",
          type: 'line',
        },
        stroke: {
          width: 5,
          curve: 'smooth'
        },
        xaxis: {
          type: 'datetime',
          categories: ['1/11/2000', '2/11/2000', '3/11/2000', '4/11/2000', '5/11/2000', '6/11/2000', '7/11/2000', '8/11/2000', '9/11/2000', '10/11/2000', '11/11/2000', '12/11/2000', '1/11/2001', '2/11/2001', '3/11/2001','4/11/2001' ,'5/11/2001' ,'6/11/2001'],
          tickAmount: 10,
          labels: {
            formatter: function(value : any, timestamp : number, opts : any) {
              return opts.dateFormatter(new Date(timestamp), 'dd MMM')
            }
          }
        },
        title: {
          text: '',
          align: 'left',
          style: {
            fontSize: "16px",
            color: '#666'
          }
        },
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            gradientToColors: [ '#002665'],
            shadeIntensity: 1,
            type: 'horizontal',
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 100, 100, 100]
          },
        }
        };
    
    if(document.getElementById("line-chart") && typeof ApexCharts !== 'undefined') {
     const chart = new ApexCharts(document.getElementById("line-chart"), options);
     chart.render();
    }
    
    })
    </script>
  