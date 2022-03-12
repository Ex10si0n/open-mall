module.exports = {
    content: [
        "./index.html",
        "./src/**/*.{vue,js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            screens: {
                'hover-hover': { 'raw': '(hover: hover) and (pointer: fine)' },
            }
        },
    },
    plugins: [],
}
