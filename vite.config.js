import react from "@vitejs/plugin-react-swc";
import { defineConfig } from "vite";
import checker from "vite-plugin-checker";

export default defineConfig({
  build: {
    cssCodeSplit: false,
  },
  plugins: [
    /**
     * Babel 컴파일러를 사용하는 @vitejs/plugin-react 대신에
     * 속도가 개선된 SWC 컴파일러를 적용한 @vitejs/plugin-react-swc을 사용해요.
     */
    react(),
    checker({
      typescript: true,
    }),
  ],
});
