from django.db import models


class RiskType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class RiskField(models.Model):
    name = models.CharField(max_length=200)
    api_type = models.TextField()
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.risk_type.name, self.name)

    class Meta:
        ordering = ("risk_type", "name")


class RiskEnum(models.Model):
    """Possible values for a given enum RiskField."""
    value = models.TextField()
    field = models.ForeignKey(RiskField, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - ENUM {}".format(str(self.field), self.value)

    class Meta:
        ordering = ("field", "value")


class RiskInstance(models.Model):
    """Represents an instance of a RiskType."""
    risk_type = models.ForeignKey(RiskType, on_delete=models.CASCADE)


class RiskValue(models.Model):
    """Represents the values of the fields a RiskInstance has."""
    risk_object = models.ForeignKey(
        RiskInstance,
        on_delete=models.CASCADE,
        primary_key=True)
    risk_field = models.ForeignKey(
        RiskField,
        on_delete=models.CASCADE,
        primary_key=True)
    value = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=["risk_object"])
        ]

        unique_together = ("risk_object", "risk_field")
