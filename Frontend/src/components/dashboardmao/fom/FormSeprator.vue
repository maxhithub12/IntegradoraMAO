<script setup lang="ts">
import { ref } from 'vue';
const show2 = ref(true);
const show3 = ref(true);

/*Location Select*/
const select = ref('');
const location = ref(['Queja', 'Sugerencia']);
const selectlng = ref('');
const lang = ref(['Pendiente', 'En proceso','Resuelto']);
</script>
<template>
    <v-card elevation="10" >
        
        <v-divider></v-divider>
        <!----Account Details---->
        <v-card-text class="">
            <h6 class="text-h6">Cuentanos tu experiencia</h6>
            <v-row class="mt-5 ">
                <v-col cols="12">
                <v-label class="font-weight-medium mb-2">Comentario</v-label>
                    <VTextarea
                        auto-grow
                        placeholder="¿ Como te sentiste en las instalaciones ?"
                        rows="8"
                        color="primary"
                        row-height="30"
                        shaped
                        hide-details
                    ></VTextarea>
                </v-col>
            </v-row>
            <v-row class="align-center mb-3">
                    <v-col cols="12" sm="9" offset-sm="3">
                        <v-btn color="primary" flat>Enviar</v-btn>
                        <v-btn class="bg-lighterror text-error ml-4" flat>Cancel</v-btn>
                    </v-col>
            </v-row>
        </v-card-text>
        
    </v-card>
</template>
