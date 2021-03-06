class SimdType(object):
    """Base class for all SIMD Types."""

    def codegen(self, indent=0):
        from ctree.simd.codegen import SimdCodeGen

        return SimdCodeGen().visit(self)


class m256d(SimdType):
    pass

class m256(SimdType):
    pass

class m512(SimdType):
    pass
