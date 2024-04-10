<script setup lang="ts">
import { ref } from "vue";

import BaseBreadcrumb from "@/components/shared/BaseBreadcrumb.vue";
import WelcomeCard from "@/components/dashboardmao/analytical/WelcomeCard.vue";
import TheEarnings from "@/components/dashboardmao/analytical/TheEarnings.vue";
import MonthlyRevenue from "@/components/dashboardmao/analytical/MonthlyRevenue.vue";
import TheSalesOverview from "@/components/dashboardmao/analytical/TheSalesOverview.vue";
import TotalSales from "@/components/dashboardmao/analytical/TotalSales.vue";
import ProductMonthTable from "@/components/dashboardmao/analytical/ProductMonthTable.vue";
import BlogCard from "@/components/dashboardmao/analytical/BlogCard.vue";
import WeeklyStats from "@/components/dashboardmao/analytical/WeeklyStats.vue";
import DailyActivities from "@/components/dashboardmao/analytical/DailyActivities.vue";
import EditableTable from '@/components/table/EditableTable.vue';

const page = ref({ title: "Q & S" });
const breadcrumbs = ref([
  {
    text: "Dashboard",
    disabled: false,
    href: "#",
  },
  {
    text: "Quejas y Sugerencias",
    disabled: true,
    href: "#",
  },
]);
</script>

<template>
  <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
  <v-row>
    <!---Welcome cards / Earnings / monthlyrevenue-->
    <!-- <v-col cols="12" sm="12" lg="6">
      <WelcomeCard />
      <v-row class="mt-4">
        <v-col cols="12" sm="6" lg="6" class="">
          <TheEarnings/>
        </v-col>
        <v-col cols="12" sm="6" lg="6" class="">
          <MonthlyRevenue/>
        </v-col>
      </v-row>
    </v-col> -->
    <v-row>
        <v-col cols="12">
            <UiParentCard title="Editable Table">
                <EditableTable />
            </UiParentCard>
        </v-col>
    </v-row>
     <!---Product month table-->
    <v-col cols="12" sm="12" lg="8">
      <ProductMonthTable/>
    </v-col>
     <!---Blog card-->
    <v-col cols="12" sm="12" lg="4">
      <BlogCard/>
    </v-col>
    
  </v-row>
</template>
