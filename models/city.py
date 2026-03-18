from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_float(x: Any) -> float:
    assert isinstance(x, (int, float))
    return x


class LocalNames:
    be: str
    el: str
    bn: str
    az: str
    en: str
    la: str
    zh: str
    sr: str
    nl: str
    de: str
    eo: str
    lt: str
    fr: str
    ka: str
    uk: str
    es: str
    it: str
    eu: str
    feature_name: str
    ar: str
    ca: str
    ascii: str
    cs: str
    am: str
    tr: str
    lv: str
    ru: str
    pl: str
    oc: str

    def __init__(self, be: str, el: str, bn: str, az: str, en: str, la: str, zh: str, sr: str, nl: str, de: str, eo: str, lt: str, fr: str, ka: str, uk: str, es: str, it: str, eu: str, feature_name: str, ar: str, ca: str, ascii: str, cs: str, am: str, tr: str, lv: str, ru: str, pl: str, oc: str) -> None:
        self.be = be
        self.el = el
        self.bn = bn
        self.az = az
        self.en = en
        self.la = la
        self.zh = zh
        self.sr = sr
        self.nl = nl
        self.de = de
        self.eo = eo
        self.lt = lt
        self.fr = fr
        self.ka = ka
        self.uk = uk
        self.es = es
        self.it = it
        self.eu = eu
        self.feature_name = feature_name
        self.ar = ar
        self.ca = ca
        self.ascii = ascii
        self.cs = cs
        self.am = am
        self.tr = tr
        self.lv = lv
        self.ru = ru
        self.pl = pl
        self.oc = oc

    @staticmethod
    def from_dict(obj: Any) -> 'LocalNames':
        assert isinstance(obj, dict)
        be = from_str(obj.get("be"))
        el = from_str(obj.get("el"))
        bn = from_str(obj.get("bn"))
        az = from_str(obj.get("az"))
        en = from_str(obj.get("en"))
        la = from_str(obj.get("la"))
        zh = from_str(obj.get("zh"))
        sr = from_str(obj.get("sr"))
        nl = from_str(obj.get("nl"))
        de = from_str(obj.get("de"))
        eo = from_str(obj.get("eo"))
        lt = from_str(obj.get("lt"))
        fr = from_str(obj.get("fr"))
        ka = from_str(obj.get("ka"))
        uk = from_str(obj.get("uk"))
        es = from_str(obj.get("es"))
        it = from_str(obj.get("it"))
        eu = from_str(obj.get("eu"))
        feature_name = from_str(obj.get("feature_name"))
        ar = from_str(obj.get("ar"))
        ca = from_str(obj.get("ca"))
        ascii = from_str(obj.get("ascii"))
        cs = from_str(obj.get("cs"))
        am = from_str(obj.get("am"))
        tr = from_str(obj.get("tr"))
        lv = from_str(obj.get("lv"))
        ru = from_str(obj.get("ru"))
        pl = from_str(obj.get("pl"))
        oc = from_str(obj.get("oc"))
        return LocalNames(be, el, bn, az, en, la, zh, sr, nl, de, eo, lt, fr, ka, uk, es, it, eu, feature_name, ar, ca, ascii, cs, am, tr, lv, ru, pl, oc)

    def to_dict(self) -> dict:
        result: dict = {}
        result["be"] = from_str(self.be)
        result["el"] = from_str(self.el)
        result["bn"] = from_str(self.bn)
        result["az"] = from_str(self.az)
        result["en"] = from_str(self.en)
        result["la"] = from_str(self.la)
        result["zh"] = from_str(self.zh)
        result["sr"] = from_str(self.sr)
        result["nl"] = from_str(self.nl)
        result["de"] = from_str(self.de)
        result["eo"] = from_str(self.eo)
        result["lt"] = from_str(self.lt)
        result["fr"] = from_str(self.fr)
        result["ka"] = from_str(self.ka)
        result["uk"] = from_str(self.uk)
        result["es"] = from_str(self.es)
        result["it"] = from_str(self.it)
        result["eu"] = from_str(self.eu)
        result["feature_name"] = from_str(self.feature_name)
        result["ar"] = from_str(self.ar)
        result["ca"] = from_str(self.ca)
        result["ascii"] = from_str(self.ascii)
        result["cs"] = from_str(self.cs)
        result["am"] = from_str(self.am)
        result["tr"] = from_str(self.tr)
        result["lv"] = from_str(self.lv)
        result["ru"] = from_str(self.ru)
        result["pl"] = from_str(self.pl)
        result["oc"] = from_str(self.oc)
        return result


class City:
    name: str
    local_names: LocalNames
    lat: float
    lon: float
    country: str
    state: str

    def __init__(self, name: str, local_names: LocalNames, lat: float, lon: float, country: str, state: str) -> None:
        self.name = name
        self.local_names = local_names
        self.lat = lat
        self.lon = lon
        self.country = country
        self.state = state

    @staticmethod
    def from_dict(obj: Any) -> 'City':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        local_names = LocalNames.from_dict(obj.get("local_names"))
        lat = from_float(obj.get("lat"))
        lon = from_float(obj.get("lon"))
        country = from_str(obj.get("country"))
        state = from_str(obj.get("state"))
        return City(name, local_names, lat, lon, country, state)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["local_names"] = to_class(LocalNames, self.local_names)
        result["lat"] = to_float(self.lat)
        result["lon"] = to_float(self.lon)
        result["country"] = from_str(self.country)
        result["state"] = from_str(self.state)
        return result


def city_from_dict(s: Any) -> City:
    return City.from_dict(s)


def city_to_dict(x: City) -> Any:
    return to_class(City, x)
