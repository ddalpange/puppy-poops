/**
 * 참고:
 * 공용으로 사용되는 CSS를 index.ts에 포함시켜서,
 * Code Splitting으로 인한 과도한 번들 사이즈 증가를 막습니다.
 */
import "./global.css";
import "normalize.css";

import React from "react";
import ReactDOM from "react-dom/client";

import App from "./App";

/**
 * React 18와 Concurrent Rendering을 사용합니다.
 * Stackflow는 startTransition을 적극적으로 활용하고 있습니다.
 * Preloading 등의 테크닉을 통해 JavaScript 코드와 API 콜을 동시에 수행하세요.
 */
const root = ReactDOM.createRoot(document.getElementById("root")!);
root.render(<App />);
