# The contents of this file are automatically generated
# 2018-02-16 13:18:54

from . import core
from altair.utils.schemapi import Undefined
from altair.utils import parse_shorthand, parse_shorthand_plus_data


class Color(core.MarkPropFieldDefWithCondition):
    """Color channel; a simple wrapper of core.MarkPropFieldDefWithCondition
    
    A FieldDef with Condition<ValueDef> {    condition: {value: ...},    field: ...,    ... }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    condition : anyOf(ConditionalValueDef, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A field definition's `condition` property can only contain [value definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def) since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    legend : anyOf(Legend, None)
        An object defining properties of the legend. If `null`, the legend for the encoding channel will be removed.  __Default value:__ If undefined, default [legend properties](https://vega.github.io/vega-lite/docs/legend.html) are applied.
    scale : Scale
        An object defining properties of the channel's scale, which is the function that transforms values in the data domain (numbers, dates, strings, etc) to visual values (pixels, colors, sizes) of the encoding channels.  __Default value:__ If undefined, default [scale properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include `"ascending"`, `"descending"` and `null` (no sorting). For fields with discrete domains, `sort` can also be a [sort field definition object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).  __Default value:__ `"ascending"`
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Color, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Color, self).to_dict(validate=validate, ignore=ignore, context=context)


class ColorValue(core.MarkPropValueDefWithCondition):
    """Color channel; a simple wrapper of core.MarkPropValueDefWithCondition
    
    A ValueDef with Condition<ValueDef | FieldDef> {    condition: {field: ...} | {value: ...},    value: ..., }
    
    Attributes
    ----------
    condition : anyOf(ConditionalMarkPropFieldDef, ConditionalValueDef, list)
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, *args, **kwargs):
        super(ColorValue, self).__init__(value=value, *args, **kwargs)


class Column(core.FacetFieldDef):
    """Column channel; a simple wrapper of core.FacetFieldDef
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    header : Header
        An object defining properties of a facet's header.
    sort : SortOrder
        Sort order for a facet field. This can be `"ascending"`, `"descending"`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Column, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Column, self).to_dict(validate=validate, ignore=ignore, context=context)


class Detail(core.FieldDef):
    """Detail channel; a simple wrapper of core.FieldDef
    
    Definition object for a data field, its type and transformation of an encoding channel.
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Detail, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Detail, self).to_dict(validate=validate, ignore=ignore, context=context)


class Href(core.FieldDefWithCondition):
    """Href channel; a simple wrapper of core.FieldDefWithCondition
    
    A FieldDef with Condition<ValueDef> {    condition: {value: ...},    field: ...,    ... }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    condition : anyOf(ConditionalValueDef, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A field definition's `condition` property can only contain [value definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def) since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Href, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Href, self).to_dict(validate=validate, ignore=ignore, context=context)


class HrefValue(core.ValueDefWithCondition):
    """Href channel; a simple wrapper of core.ValueDefWithCondition
    
    A ValueDef with Condition<ValueDef | FieldDef> {    condition: {field: ...} | {value: ...},    value: ..., }
    
    Attributes
    ----------
    condition : anyOf(ConditionalFieldDef, ConditionalValueDef, list)
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, *args, **kwargs):
        super(HrefValue, self).__init__(value=value, *args, **kwargs)


class Opacity(core.MarkPropFieldDefWithCondition):
    """Opacity channel; a simple wrapper of core.MarkPropFieldDefWithCondition
    
    A FieldDef with Condition<ValueDef> {    condition: {value: ...},    field: ...,    ... }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    condition : anyOf(ConditionalValueDef, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A field definition's `condition` property can only contain [value definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def) since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    legend : anyOf(Legend, None)
        An object defining properties of the legend. If `null`, the legend for the encoding channel will be removed.  __Default value:__ If undefined, default [legend properties](https://vega.github.io/vega-lite/docs/legend.html) are applied.
    scale : Scale
        An object defining properties of the channel's scale, which is the function that transforms values in the data domain (numbers, dates, strings, etc) to visual values (pixels, colors, sizes) of the encoding channels.  __Default value:__ If undefined, default [scale properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include `"ascending"`, `"descending"` and `null` (no sorting). For fields with discrete domains, `sort` can also be a [sort field definition object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).  __Default value:__ `"ascending"`
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Opacity, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Opacity, self).to_dict(validate=validate, ignore=ignore, context=context)


class OpacityValue(core.MarkPropValueDefWithCondition):
    """Opacity channel; a simple wrapper of core.MarkPropValueDefWithCondition
    
    A ValueDef with Condition<ValueDef | FieldDef> {    condition: {field: ...} | {value: ...},    value: ..., }
    
    Attributes
    ----------
    condition : anyOf(ConditionalMarkPropFieldDef, ConditionalValueDef, list)
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, *args, **kwargs):
        super(OpacityValue, self).__init__(value=value, *args, **kwargs)


class Order(core.OrderFieldDef):
    """Order channel; a simple wrapper of core.OrderFieldDef
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    sort : SortOrder
        The sort order. One of `"ascending"` (default) or `"descending"`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Order, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Order, self).to_dict(validate=validate, ignore=ignore, context=context)


class Row(core.FacetFieldDef):
    """Row channel; a simple wrapper of core.FacetFieldDef
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    header : Header
        An object defining properties of a facet's header.
    sort : SortOrder
        Sort order for a facet field. This can be `"ascending"`, `"descending"`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Row, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Row, self).to_dict(validate=validate, ignore=ignore, context=context)


class Shape(core.MarkPropFieldDefWithCondition):
    """Shape channel; a simple wrapper of core.MarkPropFieldDefWithCondition
    
    A FieldDef with Condition<ValueDef> {    condition: {value: ...},    field: ...,    ... }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    condition : anyOf(ConditionalValueDef, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A field definition's `condition` property can only contain [value definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def) since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    legend : anyOf(Legend, None)
        An object defining properties of the legend. If `null`, the legend for the encoding channel will be removed.  __Default value:__ If undefined, default [legend properties](https://vega.github.io/vega-lite/docs/legend.html) are applied.
    scale : Scale
        An object defining properties of the channel's scale, which is the function that transforms values in the data domain (numbers, dates, strings, etc) to visual values (pixels, colors, sizes) of the encoding channels.  __Default value:__ If undefined, default [scale properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include `"ascending"`, `"descending"` and `null` (no sorting). For fields with discrete domains, `sort` can also be a [sort field definition object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).  __Default value:__ `"ascending"`
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Shape, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Shape, self).to_dict(validate=validate, ignore=ignore, context=context)


class ShapeValue(core.MarkPropValueDefWithCondition):
    """Shape channel; a simple wrapper of core.MarkPropValueDefWithCondition
    
    A ValueDef with Condition<ValueDef | FieldDef> {    condition: {field: ...} | {value: ...},    value: ..., }
    
    Attributes
    ----------
    condition : anyOf(ConditionalMarkPropFieldDef, ConditionalValueDef, list)
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, *args, **kwargs):
        super(ShapeValue, self).__init__(value=value, *args, **kwargs)


class Size(core.MarkPropFieldDefWithCondition):
    """Size channel; a simple wrapper of core.MarkPropFieldDefWithCondition
    
    A FieldDef with Condition<ValueDef> {    condition: {value: ...},    field: ...,    ... }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    condition : anyOf(ConditionalValueDef, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A field definition's `condition` property can only contain [value definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def) since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    legend : anyOf(Legend, None)
        An object defining properties of the legend. If `null`, the legend for the encoding channel will be removed.  __Default value:__ If undefined, default [legend properties](https://vega.github.io/vega-lite/docs/legend.html) are applied.
    scale : Scale
        An object defining properties of the channel's scale, which is the function that transforms values in the data domain (numbers, dates, strings, etc) to visual values (pixels, colors, sizes) of the encoding channels.  __Default value:__ If undefined, default [scale properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include `"ascending"`, `"descending"` and `null` (no sorting). For fields with discrete domains, `sort` can also be a [sort field definition object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).  __Default value:__ `"ascending"`
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Size, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Size, self).to_dict(validate=validate, ignore=ignore, context=context)


class SizeValue(core.MarkPropValueDefWithCondition):
    """Size channel; a simple wrapper of core.MarkPropValueDefWithCondition
    
    A ValueDef with Condition<ValueDef | FieldDef> {    condition: {field: ...} | {value: ...},    value: ..., }
    
    Attributes
    ----------
    condition : anyOf(ConditionalMarkPropFieldDef, ConditionalValueDef, list)
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, *args, **kwargs):
        super(SizeValue, self).__init__(value=value, *args, **kwargs)


class Text(core.TextFieldDefWithCondition):
    """Text channel; a simple wrapper of core.TextFieldDefWithCondition
    
    A FieldDef with Condition<ValueDef> {    condition: {value: ...},    field: ...,    ... }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    condition : anyOf(ConditionalValueDef, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A field definition's `condition` property can only contain [value definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def) since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    format : string
        The [formatting pattern](https://vega.github.io/vega-lite/docs/format.html) for a text field. If not defined, this will be determined automatically.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Text, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Text, self).to_dict(validate=validate, ignore=ignore, context=context)


class TextValue(core.TextValueDefWithCondition):
    """Text channel; a simple wrapper of core.TextValueDefWithCondition
    
    A ValueDef with Condition<ValueDef | FieldDef> {    condition: {field: ...} | {value: ...},    value: ..., }
    
    Attributes
    ----------
    condition : anyOf(ConditionalTextFieldDef, ConditionalValueDef, list)
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, *args, **kwargs):
        super(TextValue, self).__init__(value=value, *args, **kwargs)


class Tooltip(core.TextFieldDefWithCondition):
    """Tooltip channel; a simple wrapper of core.TextFieldDefWithCondition
    
    A FieldDef with Condition<ValueDef> {    condition: {value: ...},    field: ...,    ... }
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    condition : anyOf(ConditionalValueDef, list)
        One or more value definition(s) with a selection predicate.  __Note:__ A field definition's `condition` property can only contain [value definitions](https://vega.github.io/vega-lite/docs/encoding.html#value-def) since Vega-Lite only allows at most one encoded field per encoding channel.
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    format : string
        The [formatting pattern](https://vega.github.io/vega-lite/docs/format.html) for a text field. If not defined, this will be determined automatically.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Tooltip, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Tooltip, self).to_dict(validate=validate, ignore=ignore, context=context)


class TooltipValue(core.TextValueDefWithCondition):
    """Tooltip channel; a simple wrapper of core.TextValueDefWithCondition
    
    A ValueDef with Condition<ValueDef | FieldDef> {    condition: {field: ...} | {value: ...},    value: ..., }
    
    Attributes
    ----------
    condition : anyOf(ConditionalTextFieldDef, ConditionalValueDef, list)
        A field definition or one or more value definition(s) with a selection predicate.
    value : anyOf(float, string, boolean)
        A constant value in visual domain.
    """
    def __init__(self, value, *args, **kwargs):
        super(TooltipValue, self).__init__(value=value, *args, **kwargs)


class X(core.PositionFieldDef):
    """X channel; a simple wrapper of core.PositionFieldDef
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    axis : anyOf(Axis, None)
        An object defining properties of axis's gridlines, ticks and labels. If `null`, the axis for the encoding channel will be removed.  __Default value:__ If undefined, default [axis properties](https://vega.github.io/vega-lite/docs/axis.html) are applied.
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    scale : Scale
        An object defining properties of the channel's scale, which is the function that transforms values in the data domain (numbers, dates, strings, etc) to visual values (pixels, colors, sizes) of the encoding channels.  __Default value:__ If undefined, default [scale properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include `"ascending"`, `"descending"` and `null` (no sorting). For fields with discrete domains, `sort` can also be a [sort field definition object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).  __Default value:__ `"ascending"`
    stack : anyOf(StackOffset, None)
        Type of stacking offset if the field should be stacked. `stack` is only applicable for `x` and `y` channels with continuous domains. For example, `stack` of `y` can be used to customize stacking for a vertical bar chart.  `stack` can be one of the following values: - `"zero"`: stacking with baseline offset at zero value of the scale (for creating typical stacked [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and [area](https://vega.github.io/vega-lite/docs/stack.html#area) chart). - `"normalize"` - stacking with normalized domain (for creating [normalized stacked bar and area charts](https://vega.github.io/vega-lite/docs/stack.html#normalized). <br/> -`"center"` - stacking with center baseline (for [streamgraph](https://vega.github.io/vega-lite/docs/stack.html#streamgraph)). - `null` - No-stacking. This will produce layered [bar](https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart) and area chart.  __Default value:__ `zero` for plots with all of the following conditions are true: (1) the mark is `bar` or `area`; (2) the stacked measure channel (x or y) has a linear scale; (3) At least one of non-position channels mapped to an unaggregated field that is different from x and y.  Otherwise, `null` by default.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(X, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(X, self).to_dict(validate=validate, ignore=ignore, context=context)


class XValue(core.ValueDef):
    """X channel; a simple wrapper of core.ValueDef
    
    Definition object for a constant value of an encoding channel.
    
    Attributes
    ----------
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., `"red"` / "#0099ff" for color, values between `0` to `1` for opacity).
    """
    def __init__(self, value, *args, **kwargs):
        super(XValue, self).__init__(value=value, *args, **kwargs)


class X2(core.FieldDef):
    """X2 channel; a simple wrapper of core.FieldDef
    
    Definition object for a data field, its type and transformation of an encoding channel.
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(X2, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(X2, self).to_dict(validate=validate, ignore=ignore, context=context)


class X2Value(core.ValueDef):
    """X2 channel; a simple wrapper of core.ValueDef
    
    Definition object for a constant value of an encoding channel.
    
    Attributes
    ----------
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., `"red"` / "#0099ff" for color, values between `0` to `1` for opacity).
    """
    def __init__(self, value, *args, **kwargs):
        super(X2Value, self).__init__(value=value, *args, **kwargs)


class Y(core.PositionFieldDef):
    """Y channel; a simple wrapper of core.PositionFieldDef
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    axis : anyOf(Axis, None)
        An object defining properties of axis's gridlines, ticks and labels. If `null`, the axis for the encoding channel will be removed.  __Default value:__ If undefined, default [axis properties](https://vega.github.io/vega-lite/docs/axis.html) are applied.
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    scale : Scale
        An object defining properties of the channel's scale, which is the function that transforms values in the data domain (numbers, dates, strings, etc) to visual values (pixels, colors, sizes) of the encoding channels.  __Default value:__ If undefined, default [scale properties](https://vega.github.io/vega-lite/docs/scale.html) are applied.
    sort : anyOf(SortOrder, SortField, None)
        Sort order for the encoded field. Supported `sort` values include `"ascending"`, `"descending"` and `null` (no sorting). For fields with discrete domains, `sort` can also be a [sort field definition object](https://vega.github.io/vega-lite/docs/sort.html#sort-field).  __Default value:__ `"ascending"`
    stack : anyOf(StackOffset, None)
        Type of stacking offset if the field should be stacked. `stack` is only applicable for `x` and `y` channels with continuous domains. For example, `stack` of `y` can be used to customize stacking for a vertical bar chart.  `stack` can be one of the following values: - `"zero"`: stacking with baseline offset at zero value of the scale (for creating typical stacked [bar](https://vega.github.io/vega-lite/docs/stack.html#bar) and [area](https://vega.github.io/vega-lite/docs/stack.html#area) chart). - `"normalize"` - stacking with normalized domain (for creating [normalized stacked bar and area charts](https://vega.github.io/vega-lite/docs/stack.html#normalized). <br/> -`"center"` - stacking with center baseline (for [streamgraph](https://vega.github.io/vega-lite/docs/stack.html#streamgraph)). - `null` - No-stacking. This will produce layered [bar](https://vega.github.io/vega-lite/docs/stack.html#layered-bar-chart) and area chart.  __Default value:__ `zero` for plots with all of the following conditions are true: (1) the mark is `bar` or `area`; (2) the stacked measure channel (x or y) has a linear scale; (3) At least one of non-position channels mapped to an unaggregated field that is different from x and y.  Otherwise, `null` by default.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Y, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Y, self).to_dict(validate=validate, ignore=ignore, context=context)


class YValue(core.ValueDef):
    """Y channel; a simple wrapper of core.ValueDef
    
    Definition object for a constant value of an encoding channel.
    
    Attributes
    ----------
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., `"red"` / "#0099ff" for color, values between `0` to `1` for opacity).
    """
    def __init__(self, value, *args, **kwargs):
        super(YValue, self).__init__(value=value, *args, **kwargs)


class Y2(core.FieldDef):
    """Y2 channel; a simple wrapper of core.FieldDef
    
    Definition object for a data field, its type and transformation of an encoding channel.
    
    Attributes
    ----------
    aggregate : Aggregate
        Aggregation function for the field (e.g., `mean`, `sum`, `median`, `min`, `max`, `count`).  __Default value:__ `undefined` (None)
    bin : anyOf(boolean, BinParams)
        A flag for binning a `quantitative` field, or [an object defining binning parameters](https://vega.github.io/vega-lite/docs/bin.html#params). If `true`, default [binning parameters](https://vega.github.io/vega-lite/docs/bin.html) will be applied.  __Default value:__ `false`
    field : anyOf(string, RepeatRef)
        __Required.__ A string defining the name of the field from which to pull a data value or an object defining iterated values from the [`repeat`](https://vega.github.io/vega-lite/docs/repeat.html) operator.  __Note:__ Dots (`.`) and brackets (`[` and `]`) can be used to access nested objects (e.g., `"field": "foo.bar"` and `"field": "foo['bar']"`). If field names contain dots or brackets but are not nested, you can use `\\` to escape dots and brackets (e.g., `"a\\.b"` and `"a\\[0\\]"`). See more details about escaping in the [field documentation](https://vega.github.io/vega-lite/docs/field.html).  __Note:__ `field` is not required if `aggregate` is `count`.
    timeUnit : TimeUnit
        Time unit (e.g., `year`, `yearmonth`, `month`, `hours`) for a temporal field. or [a temporal field that gets casted as ordinal](https://vega.github.io/vega-lite/docs/type.html#cast).  __Default value:__ `undefined` (None)
    type : Type
        The encoded field's type of measurement (`"quantitative"`, `"temporal"`, `"ordinal"`, or `"nominal"`). It can also be a geo type (`"latitude"`, `"longitude"`, and `"geojson"`) when a [geographic projection](https://vega.github.io/vega-lite/docs/projection.html) is applied.
    """
    def __init__(self, field, **kwargs):
        super(Y2, self).__init__(field=field, **kwargs)

    def to_dict(self, validate=True, ignore=[], context={}):
        type_ = getattr(self, 'type', Undefined)
        if type_ is Undefined and 'data' in context:
            kwds = parse_shorthand_plus_data(self.field, context['data'])
        else:
            kwds = parse_shorthand(self.field)
        self._kwds.update(kwds)
        return super(Y2, self).to_dict(validate=validate, ignore=ignore, context=context)


class Y2Value(core.ValueDef):
    """Y2 channel; a simple wrapper of core.ValueDef
    
    Definition object for a constant value of an encoding channel.
    
    Attributes
    ----------
    value : anyOf(float, string, boolean)
        A constant value in visual domain (e.g., `"red"` / "#0099ff" for color, values between `0` to `1` for opacity).
    """
    def __init__(self, value, *args, **kwargs):
        super(Y2Value, self).__init__(value=value, *args, **kwargs)
