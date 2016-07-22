
package us.kbase.subdataselectiontester;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: SubObjectIdentity</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "ref",
    "included"
})
public class SubObjectIdentity {

    @JsonProperty("ref")
    private java.lang.String ref;
    @JsonProperty("included")
    private List<String> included;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("ref")
    public java.lang.String getRef() {
        return ref;
    }

    @JsonProperty("ref")
    public void setRef(java.lang.String ref) {
        this.ref = ref;
    }

    public SubObjectIdentity withRef(java.lang.String ref) {
        this.ref = ref;
        return this;
    }

    @JsonProperty("included")
    public List<String> getIncluded() {
        return included;
    }

    @JsonProperty("included")
    public void setIncluded(List<String> included) {
        this.included = included;
    }

    public SubObjectIdentity withIncluded(List<String> included) {
        this.included = included;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((("SubObjectIdentity"+" [ref=")+ ref)+", included=")+ included)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
