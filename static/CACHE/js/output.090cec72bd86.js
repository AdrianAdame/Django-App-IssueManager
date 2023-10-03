window.onload=()=>{dayjs().format()
dayjs.extend(window.dayjs_plugin_relativeTime)
console.log(dayjs('11-26-2001').fromNow())};