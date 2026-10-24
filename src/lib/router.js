// Tiny hash router. Hash URLs (#/course/x) work on GitHub Pages without
// any server setup, and a refresh never shows a 404.

import { useEffect, useState } from 'react'
import { parseRoute, hrefFor } from './routes.js'

export { parseRoute, hrefFor }

export function navigate(route) {
  window.location.hash = hrefFor(route)
}

export function useRoute() {
  const [route, setRoute] = useState(() => parseRoute(window.location.hash))
  useEffect(() => {
    const onChange = () => {
      setRoute(parseRoute(window.location.hash))
      window.scrollTo(0, 0)
    }
    window.addEventListener('hashchange', onChange)
    return () => window.removeEventListener('hashchange', onChange)
  }, [])
  return route
}
