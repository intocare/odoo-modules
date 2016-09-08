# odoo-pubsub

> Publish changes of a model to an external API


## Usage

There are two steps that have to be performed in order to receive updates to an API endpoint.

### Configure endpoint

1. Create a new endpoint in `Settings > PubSub`.
2. Provide a `Name` and an `Endpoint` url.
3. You can add custom headers in the `Headers` tab.

### Add an automated action

The PubSub module does not subscribe directly to changes in other models. It relies on the Odoo automated actions to notify this module.

1. Create a new automated action in the `Settings > Automation > Automated Actions` menu.
2. Provide a `Rule Name` and select the `Related Document Model`. This is the model where you want to receive updates for.
3. Create a new `Server Action` and select `Create or Copy a new Record` in the `Action To Do` dropdown.
4. Open the `Create / Write / Copy` tab.
  1. Select `Create a new record in another model`.
  2. Use `pubsub.data` as `Target Model`.
  3. Add some custom [Value Mapping](#value-mapping) records.

#### Value Mapping

The value mappings are used to map the original record, our base model record, to a `pubsub.data` record. That model has three properties.

##### Ref

*Required*<br>
Evaluation Type: `Python expression`<br>
Value: `obj.id`

The ID of the record that was created.

##### Type

*Required*<br>
Evaluation Type: `Value`

Identifier that can be used at server level in order to retrieve the updated record. For instance, the name of the model.

##### Data

Evaluation Type: `Python expression`

Optional object with extra data that will be send to the server. The value should look like `{'foo': 'bar'}`.


## Filter types

When configuring your endpoint, you can add multiple types in the `Types` section. If no type is added to the endpoint, the endpoint will execute for every record being created. If for instance you add the type `contact`, the endpoint will only be called if it matches the type provided in the [Value Mapping](#type).

This way, it is possible to call different API endpoints depending on the data.


## License

MIT © [Pridiktiv](http://pridiktiv.care)
