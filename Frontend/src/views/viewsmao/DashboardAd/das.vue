<script setup lang="ts">
import { ref } from "vue";
import BaseBreadcrumb from "@/components/shared/BaseBreadcrumb.vue";
import DailyActivities from "@/components/dashboardmao/dashCl/DailyActivities.vue";
import TheSalesOverview from "@/components/dashboardmao/dashCl/TheSalesOverview.vue";
import BlogPosts from '@/components/dashboardmao/blog/blogPosts.vue';


const page = ref({ title: "Blog" });
const breadcrumbs = ref([
    {
        text: "Blog",
        disabled: false,
        href: "#",
    },
    {
        text: "Usuarios",
        disabled: true,
        href: "#",
    },
]);
</script>

<template>
    <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
    <v-row>

        <v-col cols="12">
          <BlogPosts/>
        </v-col>
       
    </v-row>
</template>
