<script setup lang="ts">
import { ref } from 'vue';
// icons
import { UserIcon, BuildingArchIcon, MailIcon, PhoneIcon, Message2Icon } from 'vue-tabler-icons';
const select = ref('');
const location = ref(['Queja', 'Sugerencia']);
const selectlng = ref('');
const lang = ref(['Pendiente', 'En proceso','Resuelto']);
</script>
<template>
    <v-row>
        <v-col cols="12">
            <v-label class="font-weight-medium mb-2">Usuario</v-label>
            <v-text-field color="primary" variant="outlined" type="text" placeholder="John Deo" hide-details>
                <template v-slot:prepend-inner>
                    
                </template>
            </v-text-field>
        </v-col>
        <v-col cols="12">
            <v-label class="font-weight-medium mb-2">Tipo</v-label>
            <v-select
                            v-model="select"
                            :items="location"
                            item-title="state"
                            item-value="abbr"
                            label="Select"
                            return-object
                            single-line
                            variant="outlined"
                            hide-details
                        ></v-select>
        </v-col>
        <v-col cols="12">
            <v-label class="font-weight-medium mb-2">Estatus</v-label>
            <v-select v-model="selectlng" :items="lang" single-line variant="outlined" hide-details></v-select>
        </v-col>
        <v-col cols="12">
            <v-label class="font-weight-medium mb-2">Descripcion</v-label>
            <v-textarea
                auto-grow
                variant="outlined"
                placeholder="Hi, Do you  have a moment to talk Jeo ?"
                rows="2"
                color="primary"
                row-height="25"
                shaped
                hide-details
            >
                <template v-slot:prepend-inner>
                    
                </template>
            </v-textarea>
        </v-col>
        <v-col cols="12">
            <v-btn color="primary" flat>Enviar</v-btn>
        </v-col>
    </v-row>
</template>
