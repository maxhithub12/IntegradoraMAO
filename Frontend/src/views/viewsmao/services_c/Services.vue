<script setup lang="ts">
import { ref } from "vue";

import BaseBreadcrumb from "@/components/shared/BaseBreadcrumb.vue";
import WelcomeCard from "@/components/dashboardmao/services_c/WelcomeCard.vue";
import TheEarnings from "@/components/dashboardmao/services_c/TheEarnings.vue";
import MonthlyRevenue from "@/components/dashboardmao/services_c/MonthlyRevenue.vue";
import TheSalesOverview from "@/components/dashboardmao/services_c/TheSalesOverview.vue";
import TotalSales from "@/components/dashboardmao/services_c/TotalSales.vue";
import ProductMonthTable from "@/components/dashboardmao/services_c/ProductMonthTable.vue";
import BlogCard from "@/components/dashboardmao/services_c/BlogCard.vue";
import WeeklyStats from "@/components/dashboardmao/services_c/WeeklyStats.vue";
import DailyActivities from "@/components/dashboardmao/services_c/DailyActivities.vue";
import EditableTable from '@/components/table/EditableTable.vue';
import { BasicDatatables } from '@/_mockApis/components/datatable/dataTable';

const page = ref({ title: "Servicios" });
const breadcrumbs = ref([
  {
    text: "Servicios ",
    disabled: false,
    href: "#",
  },
  {
    text: "Servicios Clientes",
    disabled: true,
    href: "#",
  },
]);



/*Header Data*/
const headers :any = ref([
{ title: 'Id', align: 'start', key: 'name', sortable: false, },
    { title: 'Nombre Servicio', align: 'start', key: 'project' },
    { title: 'Estatus', align: 'start', key: 'status' },
    { title: 'Sucursal', align: 'end', key: 'budget' },
    { title: '', key: 'data-table-expand' },
])



/*for status color*/
function getColor(status: string) {
    if (status == 'Disponible') return '#13DEB9'
    else if (status == 'No Disponible') return '#FA896B'
    else return '#FFAE1F'
}
</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
   
    <v-col cols="12">
            

            <UiParentCard title="Item" class="mt-6">
                <v-data-table items-per-page="5" :headers="headers"  :items="BasicDatatables" item-value="name"
                    class="border rounded-md">
                    <template  v-slot:item.status="{ item }">
                        <v-chip :color="getColor(item.status)">
                            {{ item.status }}
                        </v-chip>
                    </template>
                </v-data-table>
            </UiParentCard>

           
        </v-col>
    
  </v-row>
</template>
