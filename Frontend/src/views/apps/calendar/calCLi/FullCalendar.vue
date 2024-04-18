<script>
import { defineComponent } from 'vue'
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'

let eventGuid = 0
let todayStr = new Date().toISOString().replace(/T.*$/, '') // YYYY-MM-DD of today

const today = new Date();
const y = today.getFullYear();
const m = today.getMonth();
const d = today.getDate();

export const INITIAL_EVENTS = [

  {
    id: createEventId(),
    title: 'Sesion 1',
    allDay: true,
    start: new Date(y, m, 3),
    end: new Date(y, m, 5),
    color: '#615dff',
  },
  {
    id: createEventId(),
    title: 'Sesion 7',
    start: new Date(y, m, d + 3, 10, 30),
    end: new Date(y, m, d + 3, 11, 30),
    allDay: true,
    color: '#39b69a',
  },
  {
    id: createEventId(),
    title: 'Sesion 8',
    start: new Date(y, m, d + 7, 12, 0),
    end: new Date(y, m, d + 7, 14, 0),
    allDay: true,
    color: '#fc4b6c',
  },
  {
    id: createEventId(),
    title: 'Sesion 3',
    start: new Date(y, m, d - 2),
    end: new Date(y, m, d - 2),
    allDay: true,
    color: '#1a97f5',
  },
  {
    id: createEventId(),
    title: 'Sesion 4',
    start: new Date(y, m, d + 1, 19, 0),
    end: new Date(y, m, d + 1, 22, 30),
    allDay: true,
    color: '#1a97f5',
  },
  {
    id: createEventId(),
    title: 'Sesion 5',
    start: new Date(y, m, 23),
    end: new Date(y, m, 25),
    color: '#fdd43f',
  },
  {
    id: createEventId(),
    title: 'Sesion 2',
    start: new Date(y, m, 19),
    end: new Date(y, m, 22),
    color: '615dff',
  },
]
