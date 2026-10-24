import { BackLink } from './Bits.jsx'

export default function NotFound({ what }) {
  return (
    <>
      <BackLink to={{ name: 'library' }}>All courses</BackLink>
      <h1 className="page-title">This {what} isn't here</h1>
      <p>
        The link may be from an older version of the course, or the course file was removed from this device.
      </p>
    </>
  )
}
