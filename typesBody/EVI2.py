def getBodyEVI2(x, y):
    body = f"""{{
  "expression": {{
    "result": "0",
    "values": {{
      "0": {{
        "functionInvocationValue": {{
          "arguments": {{
            "dictionary": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "collection": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "collection": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "collection": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "collection1": {{
                                      "valueReference": "1"
                                    }},
                                    "collection2": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "images": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "list": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "list": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "start": {{
                                                              "functionInvocationValue": {{
                                                                "arguments": {{
                                                                  "date": {{
                                                                    "functionInvocationValue": {{
                                                                      "arguments": {{
                                                                        "image": {{
                                                                          "functionInvocationValue": {{
                                                                            "arguments": {{
                                                                              "collection": {{
                                                                                "valueReference": "1"
                                                                              }}
                                                                            }},
                                                                            "functionName": "Collection.first"
                                                                          }}
                                                                        }}
                                                                      }},
                                                                      "functionName": "Image.date"
                                                                    }}
                                                                  }},
                                                                  "unit": {{
                                                                    "valueReference": "68"
                                                                  }}
                                                                }},
                                                                "functionName": "Date.get"
                                                              }}
                                                            }},
                                                            "end": {{
                                                              "functionInvocationValue": {{
                                                                "arguments": {{
                                                                  "date": {{
                                                                    "functionInvocationValue": {{
                                                                      "arguments": {{
                                                                        "image": {{
                                                                          "functionInvocationValue": {{
                                                                            "arguments": {{
                                                                              "collection": {{
                                                                                "functionInvocationValue": {{
                                                                                  "arguments": {{
                                                                                    "collection": {{
                                                                                      "valueReference": "1"
                                                                                    }},
                                                                                    "key": {{
                                                                                      "valueReference": "38"
                                                                                    }},
                                                                                    "ascending": {{
                                                                                      "constantValue": false
                                                                                    }}
                                                                                  }},
                                                                                  "functionName": "Collection.limit"
                                                                                }}
                                                                              }}
                                                                            }},
                                                                            "functionName": "Collection.first"
                                                                          }}
                                                                        }}
                                                                      }},
                                                                      "functionName": "Image.date"
                                                                    }}
                                                                  }},
                                                                  "unit": {{
                                                                    "valueReference": "68"
                                                                  }}
                                                                }},
                                                                "functionName": "Date.get"
                                                              }}
                                                            }},
                                                            "step": {{
                                                              "constantValue": 0.1
                                                            }}
                                                          }},
                                                          "functionName": "List.sequence"
                                                        }}
                                                      }},
                                                      "baseAlgorithm": {{
                                                        "functionDefinitionValue": {{
                                                          "argumentNames": [
                                                            "_MAPPING_VAR_0_0"
                                                          ],
                                                          "body": "69"
                                                        }}
                                                      }}
                                                    }},
                                                    "functionName": "List.map"
                                                  }}
                                                }},
                                                "baseAlgorithm": {{
                                                  "functionDefinitionValue": {{
                                                    "argumentNames": [
                                                      "_MAPPING_VAR_0_0"
                                                    ],
                                                    "body": "72"
                                                  }}
                                                }}
                                              }},
                                              "functionName": "List.map"
                                            }}
                                          }}
                                        }},
                                        "functionName": "ImageCollection.fromImages"
                                      }}
                                    }}
                                  }},
                                  "functionName": "ImageCollection.merge"
                                }}
                              }},
                              "key": {{
                                "valueReference": "38"
                              }}
                            }},
                            "functionName": "Collection.limit"
                          }}
                        }},
                        "baseAlgorithm": {{
                          "functionDefinitionValue": {{
                            "argumentNames": [
                              "_MAPPING_VAR_4_0"
                            ],
                            "body": "73"
                          }}
                        }}
                      }},
                      "functionName": "Collection.map"
                    }}
                  }},
                  "reducer": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "tupleSize": {{
                          "valueReference": "93"
                        }},
                        "numOptional": {{
                          "valueReference": "93"
                        }}
                      }},
                      "functionName": "Reducer.toList"
                    }}
                  }},
                  "selectors": {{
                    "arrayValue": {{
                      "values": [
                        {{
                          "valueReference": "92"
                        }},
                        {{
                          "valueReference": "74"
                        }},
                        {{
                          "constantValue": "h0"
                        }},
                        {{
                          "constantValue": "h1"
                        }},
                        {{
                          "constantValue": "h2"
                        }},
                        {{
                          "constantValue": "h3"
                        }},
                        {{
                          "constantValue": "h4"
                        }},
                        {{
                          "constantValue": "h5"
                        }},
                        {{
                          "valueReference": "80"
                        }}
                      ]
                    }}
                  }}
                }},
                "functionName": "Collection.reduceColumns"
              }}
            }},
            "key": {{
              "constantValue": "list"
            }}
          }},
          "functionName": "Dictionary.get"
        }}
      }},
      "1": {{
        "functionInvocationValue": {{
          "arguments": {{
            "collection": {{
              "valueReference": "2"
            }},
            "key": {{
              "valueReference": "38"
            }}
          }},
          "functionName": "Collection.limit"
        }}
      }},
      "2": {{
        "functionInvocationValue": {{
          "arguments": {{
            "collection": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "collection": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "collection": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "collection1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "collection1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "collection1": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "collection": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "collection": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "collection": {{
                                                              "functionInvocationValue": {{
                                                                "arguments": {{
                                                                  "id": {{
                                                                    "constantValue": "LANDSAT/LC08/C02/T1_L2"
                                                                  }}
                                                                }},
                                                                "functionName": "ImageCollection.load"
                                                              }}
                                                            }},
                                                            "filter": {{
                                                              "valueReference": "3"
                                                            }}
                                                          }},
                                                          "functionName": "Collection.filter"
                                                        }}
                                                      }},
                                                      "filter": {{
                                                        "valueReference": "4"
                                                      }}
                                                    }},
                                                    "functionName": "Collection.filter"
                                                  }}
                                                }},
                                                "baseAlgorithm": {{
                                                  "functionDefinitionValue": {{
                                                    "argumentNames": [
                                                      "_MAPPING_VAR_0_0"
                                                    ],
                                                    "body": "6"
                                                  }}
                                                }}
                                              }},
                                              "functionName": "Collection.map"
                                            }}
                                          }},
                                          "collection2": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "collection": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "collection": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "collection": {{
                                                              "functionInvocationValue": {{
                                                                "arguments": {{
                                                                  "id": {{
                                                                    "constantValue": "LANDSAT/LE07/C02/T1_L2"
                                                                  }}
                                                                }},
                                                                "functionName": "ImageCollection.load"
                                                              }}
                                                            }},
                                                            "filter": {{
                                                              "valueReference": "3"
                                                            }}
                                                          }},
                                                          "functionName": "Collection.filter"
                                                        }}
                                                      }},
                                                      "filter": {{
                                                        "valueReference": "4"
                                                      }}
                                                    }},
                                                    "functionName": "Collection.filter"
                                                  }}
                                                }},
                                                "baseAlgorithm": {{
                                                  "valueReference": "33"
                                                }}
                                              }},
                                              "functionName": "Collection.map"
                                            }}
                                          }}
                                        }},
                                        "functionName": "ImageCollection.merge"
                                      }}
                                    }},
                                    "collection2": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "collection": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "collection": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "collection": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "id": {{
                                                              "constantValue": "LANDSAT/LT05/C02/T1_L2"
                                                            }}
                                                          }},
                                                          "functionName": "ImageCollection.load"
                                                        }}
                                                      }},
                                                      "filter": {{
                                                        "valueReference": "3"
                                                      }}
                                                    }},
                                                    "functionName": "Collection.filter"
                                                  }}
                                                }},
                                                "filter": {{
                                                  "valueReference": "4"
                                                }}
                                              }},
                                              "functionName": "Collection.filter"
                                            }}
                                          }},
                                          "baseAlgorithm": {{
                                            "valueReference": "33"
                                          }}
                                        }},
                                        "functionName": "Collection.map"
                                      }}
                                    }}
                                  }},
                                  "functionName": "ImageCollection.merge"
                                }}
                              }},
                              "collection2": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "collection": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "collection": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "collection": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "id": {{
                                                        "constantValue": "LANDSAT/LT04/C02/T1_L2"
                                                      }}
                                                    }},
                                                    "functionName": "ImageCollection.load"
                                                  }}
                                                }},
                                                "filter": {{
                                                  "valueReference": "3"
                                                }}
                                              }},
                                              "functionName": "Collection.filter"
                                            }}
                                          }},
                                          "filter": {{
                                            "valueReference": "4"
                                          }}
                                        }},
                                        "functionName": "Collection.filter"
                                      }}
                                    }},
                                    "baseAlgorithm": {{
                                      "valueReference": "33"
                                    }}
                                  }},
                                  "functionName": "Collection.map"
                                }}
                              }}
                            }},
                            "functionName": "ImageCollection.merge"
                          }}
                        }},
                        "filter": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "rightField": {{
                                "valueReference": "38"
                              }},
                              "leftValue": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "start": {{
                                      "constantValue": "2000-01-01"
                                    }},
                                    "end": {{
                                      "constantValue": "2023-01-01"
                                    }}
                                  }},
                                  "functionName": "DateRange"
                                }}
                              }}
                            }},
                            "functionName": "Filter.dateRangeContains"
                          }}
                        }}
                      }},
                      "functionName": "Collection.filter"
                    }}
                  }},
                  "baseAlgorithm": {{
                    "functionDefinitionValue": {{
                      "argumentNames": [
                        "_MAPPING_VAR_0_0"
                      ],
                      "body": "39"
                    }}
                  }}
                }},
                "functionName": "Collection.map"
              }}
            }},
            "baseAlgorithm": {{
              "functionDefinitionValue": {{
                "argumentNames": [
                  "_MAPPING_VAR_0_0"
                ],
                "body": "40"
              }}
            }}
          }},
          "functionName": "Collection.map"
        }}
      }},
      "3": {{
        "constantValue": "WRS_ROW < 122"
      }},
      "4": {{
        "functionInvocationValue": {{
          "arguments": {{
            "leftField": {{
              "constantValue": ".all"
            }},
            "rightValue": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "geometry": {{
                    "valueReference": "5"
                  }}
                }},
                "functionName": "Feature"
              }}
            }}
          }},
          "functionName": "Filter.intersects"
        }}
      }},
      "5": {{
        "functionInvocationValue": {{
          "arguments": {{
            "coordinates": {{
              "constantValue": [
                {x},
                {y}
              ]
            }}
          }},
          "functionName": "GeometryConstructors.Point"
        }}
      }},
      "6": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "dstImg": {{
                    "argumentReference": "_MAPPING_VAR_0_0"
                  }},
                  "srcImg": {{
                    "valueReference": "7"
                  }}
                }},
                "functionName": "Image.addBands"
              }}
            }},
            "mask": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "image1": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image1": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "image": {{
                                            "valueReference": "24"
                                          }},
                                          "from": {{
                                            "constantValue": [
                                              21824,
                                              21888
                                            ]
                                          }},
                                          "to": {{
                                            "valueReference": "25"
                                          }},
                                          "defaultValue": {{
                                            "constantValue": 0
                                          }}
                                        }},
                                        "functionName": "Image.remap"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "26"
                                    }}
                                  }},
                                  "functionName": "Image.and"
                                }}
                              }},
                              "image2": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "image": {{
                                            "valueReference": "28"
                                          }},
                                          "reducer": {{
                                            "valueReference": "30"
                                          }}
                                        }},
                                        "functionName": "Image.reduce"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "27"
                                    }}
                                  }},
                                  "functionName": "Image.gt"
                                }}
                              }}
                            }},
                            "functionName": "Image.and"
                          }}
                        }},
                        "image2": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image": {{
                                      "valueReference": "28"
                                    }},
                                    "reducer": {{
                                      "valueReference": "31"
                                    }}
                                  }},
                                  "functionName": "Image.reduce"
                                }}
                              }},
                              "image2": {{
                                "valueReference": "32"
                              }}
                            }},
                            "functionName": "Image.lt"
                          }}
                        }}
                      }},
                      "functionName": "Image.and"
                    }}
                  }},
                  "image2": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "input": {{
                                "argumentReference": "_MAPPING_VAR_0_0"
                              }},
                              "bandSelectors": {{
                                "constantValue": [
                                  "SR_QA_AEROSOL"
                                ]
                              }}
                            }},
                            "functionName": "Image.select"
                          }}
                        }},
                        "from": {{
                          "constantValue": [
                            2,
                            4,
                            32,
                            66,
                            68,
                            96,
                            100,
                            130,
                            132,
                            160,
                            164
                          ]
                        }},
                        "to": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "value": {{
                                "constantValue": 1
                              }},
                              "count": {{
                                "constantValue": 11
                              }}
                            }},
                            "functionName": "List.repeat"
                          }}
                        }},
                        "defaultValue": {{
                          "constantValue": 0
                        }}
                      }},
                      "functionName": "Image.remap"
                    }}
                  }}
                }},
                "functionName": "Image.and"
              }}
            }}
          }},
          "functionName": "Image.updateMask"
        }}
      }},
      "7": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "input": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "dstImg": {{
                          "valueReference": "8"
                        }},
                        "srcImg": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "argumentReference": "_MAPPING_VAR_0_0"
                                          }},
                                          "bandSelectors": {{
                                            "arrayValue": {{
                                              "values": [
                                                {{
                                                  "valueReference": "9"
                                                }}
                                              ]
                                            }}
                                          }}
                                        }},
                                        "functionName": "Image.select"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "10"
                                    }}
                                  }},
                                  "functionName": "Image.multiply"
                                }}
                              }},
                              "image2": {{
                                "valueReference": "11"
                              }}
                            }},
                            "functionName": "Image.add"
                          }}
                        }},
                        "names": {{
                          "constantValue": null
                        }},
                        "overwrite": {{
                          "constantValue": true
                        }}
                      }},
                      "functionName": "Image.addBands"
                    }}
                  }},
                  "bandSelectors": {{
                    "arrayValue": {{
                      "values": [
                        {{
                          "valueReference": "12"
                        }},
                        {{
                          "valueReference": "13"
                        }},
                        {{
                          "valueReference": "14"
                        }},
                        {{
                          "valueReference": "15"
                        }},
                        {{
                          "constantValue": "SR_B6"
                        }},
                        {{
                          "valueReference": "16"
                        }},
                        {{
                          "valueReference": "9"
                        }}
                      ]
                    }}
                  }}
                }},
                "functionName": "Image.select"
              }}
            }},
            "names": {{
              "valueReference": "17"
            }}
          }},
          "functionName": "Image.rename"
        }}
      }},
      "8": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image1": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "image1": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "input": {{
                          "argumentReference": "_MAPPING_VAR_0_0"
                        }},
                        "bandSelectors": {{
                          "constantValue": [
                            "SR_B."
                          ]
                        }}
                      }},
                      "functionName": "Image.select"
                    }}
                  }},
                  "image2": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "value": {{
                          "constantValue": 0.0000275
                        }}
                      }},
                      "functionName": "Image.constant"
                    }}
                  }}
                }},
                "functionName": "Image.multiply"
              }}
            }},
            "image2": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "value": {{
                    "constantValue": -0.2
                  }}
                }},
                "functionName": "Image.constant"
              }}
            }}
          }},
          "functionName": "Image.add"
        }}
      }},
      "9": {{
        "constantValue": "ST_B10"
      }},
      "10": {{
        "functionInvocationValue": {{
          "arguments": {{
            "value": {{
              "constantValue": 0.00341802
            }}
          }},
          "functionName": "Image.constant"
        }}
      }},
      "11": {{
        "functionInvocationValue": {{
          "arguments": {{
            "value": {{
              "constantValue": 149
            }}
          }},
          "functionName": "Image.constant"
        }}
      }},
      "12": {{
        "constantValue": "SR_B2"
      }},
      "13": {{
        "constantValue": "SR_B3"
      }},
      "14": {{
        "constantValue": "SR_B4"
      }},
      "15": {{
        "constantValue": "SR_B5"
      }},
      "16": {{
        "constantValue": "SR_B7"
      }},
      "17": {{
        "arrayValue": {{
          "values": [
            {{
              "valueReference": "18"
            }},
            {{
              "valueReference": "19"
            }},
            {{
              "valueReference": "20"
            }},
            {{
              "valueReference": "21"
            }},
            {{
              "valueReference": "22"
            }},
            {{
              "valueReference": "23"
            }},
            {{
              "constantValue": "TEMP"
            }}
          ]
        }}
      }},
      "18": {{
        "constantValue": "BLUE"
      }},
      "19": {{
        "constantValue": "GREEN"
      }},
      "20": {{
        "constantValue": "RED"
      }},
      "21": {{
        "constantValue": "NIR"
      }},
      "22": {{
        "constantValue": "SWIR1"
      }},
      "23": {{
        "constantValue": "SWIR2"
      }},
      "24": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "constantValue": [
                "QA_PIXEL"
              ]
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "25": {{
        "functionInvocationValue": {{
          "arguments": {{
            "value": {{
              "constantValue": 1
            }},
            "count": {{
              "constantValue": 2
            }}
          }},
          "functionName": "List.repeat"
        }}
      }},
      "26": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image1": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "input": {{
                    "argumentReference": "_MAPPING_VAR_0_0"
                  }},
                  "bandSelectors": {{
                    "constantValue": [
                      "QA_RADSAT"
                    ]
                  }}
                }},
                "functionName": "Image.select"
              }}
            }},
            "image2": {{
              "valueReference": "27"
            }}
          }},
          "functionName": "Image.eq"
        }}
      }},
      "27": {{
        "functionInvocationValue": {{
          "arguments": {{
            "value": {{
              "constantValue": 0
            }}
          }},
          "functionName": "Image.constant"
        }}
      }},
      "28": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "valueReference": "7"
            }},
            "bandSelectors": {{
              "valueReference": "29"
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "29": {{
        "arrayValue": {{
          "values": [
            {{
              "valueReference": "18"
            }},
            {{
              "valueReference": "19"
            }},
            {{
              "valueReference": "20"
            }},
            {{
              "valueReference": "21"
            }},
            {{
              "valueReference": "22"
            }},
            {{
              "valueReference": "23"
            }}
          ]
        }}
      }},
      "30": {{
        "functionInvocationValue": {{
          "arguments": {{}},
          "functionName": "Reducer.min"
        }}
      }},
      "31": {{
        "functionInvocationValue": {{
          "arguments": {{}},
          "functionName": "Reducer.max"
        }}
      }},
      "32": {{
        "functionInvocationValue": {{
          "arguments": {{
            "value": {{
              "constantValue": 1
            }}
          }},
          "functionName": "Image.constant"
        }}
      }},
      "33": {{
        "functionDefinitionValue": {{
          "argumentNames": [
            "_MAPPING_VAR_0_0"
          ],
          "body": "34"
        }}
      }},
      "34": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "dstImg": {{
                    "argumentReference": "_MAPPING_VAR_0_0"
                  }},
                  "srcImg": {{
                    "valueReference": "35"
                  }}
                }},
                "functionName": "Image.addBands"
              }}
            }},
            "mask": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "image1": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image1": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "image": {{
                                            "valueReference": "24"
                                          }},
                                          "from": {{
                                            "constantValue": [
                                              5440,
                                              5504
                                            ]
                                          }},
                                          "to": {{
                                            "valueReference": "25"
                                          }},
                                          "defaultValue": {{
                                            "constantValue": 0
                                          }}
                                        }},
                                        "functionName": "Image.remap"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "26"
                                    }}
                                  }},
                                  "functionName": "Image.and"
                                }}
                              }},
                              "image2": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "image": {{
                                            "valueReference": "37"
                                          }},
                                          "reducer": {{
                                            "valueReference": "30"
                                          }}
                                        }},
                                        "functionName": "Image.reduce"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "27"
                                    }}
                                  }},
                                  "functionName": "Image.gt"
                                }}
                              }}
                            }},
                            "functionName": "Image.and"
                          }}
                        }},
                        "image2": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image": {{
                                      "valueReference": "37"
                                    }},
                                    "reducer": {{
                                      "valueReference": "31"
                                    }}
                                  }},
                                  "functionName": "Image.reduce"
                                }}
                              }},
                              "image2": {{
                                "valueReference": "32"
                              }}
                            }},
                            "functionName": "Image.lt"
                          }}
                        }}
                      }},
                      "functionName": "Image.and"
                    }}
                  }},
                  "image2": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image1": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "input": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "argumentReference": "_MAPPING_VAR_0_0"
                                    }},
                                    "bandSelectors": {{
                                      "constantValue": [
                                        "SR_ATMOS_OPACITY"
                                      ]
                                    }}
                                  }},
                                  "functionName": "Image.select"
                                }}
                              }},
                              "value": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "value": {{
                                      "constantValue": -1
                                    }}
                                  }},
                                  "functionName": "Image.constant"
                                }}
                              }}
                            }},
                            "functionName": "Image.unmask"
                          }}
                        }},
                        "image2": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "value": {{
                                "constantValue": 300
                              }}
                            }},
                            "functionName": "Image.constant"
                          }}
                        }}
                      }},
                      "functionName": "Image.lt"
                    }}
                  }}
                }},
                "functionName": "Image.and"
              }}
            }}
          }},
          "functionName": "Image.updateMask"
        }}
      }},
      "35": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "input": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "dstImg": {{
                          "valueReference": "8"
                        }},
                        "srcImg": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "image1": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "argumentReference": "_MAPPING_VAR_0_0"
                                          }},
                                          "bandSelectors": {{
                                            "arrayValue": {{
                                              "values": [
                                                {{
                                                  "valueReference": "36"
                                                }}
                                              ]
                                            }}
                                          }}
                                        }},
                                        "functionName": "Image.select"
                                      }}
                                    }},
                                    "image2": {{
                                      "valueReference": "10"
                                    }}
                                  }},
                                  "functionName": "Image.multiply"
                                }}
                              }},
                              "image2": {{
                                "valueReference": "11"
                              }}
                            }},
                            "functionName": "Image.add"
                          }}
                        }},
                        "names": {{
                          "constantValue": null
                        }},
                        "overwrite": {{
                          "constantValue": true
                        }}
                      }},
                      "functionName": "Image.addBands"
                    }}
                  }},
                  "bandSelectors": {{
                    "arrayValue": {{
                      "values": [
                        {{
                          "constantValue": "SR_B1"
                        }},
                        {{
                          "valueReference": "12"
                        }},
                        {{
                          "valueReference": "13"
                        }},
                        {{
                          "valueReference": "14"
                        }},
                        {{
                          "valueReference": "15"
                        }},
                        {{
                          "valueReference": "16"
                        }},
                        {{
                          "valueReference": "36"
                        }}
                      ]
                    }}
                  }}
                }},
                "functionName": "Image.select"
              }}
            }},
            "names": {{
              "valueReference": "17"
            }}
          }},
          "functionName": "Image.rename"
        }}
      }},
      "36": {{
        "constantValue": "ST_B6"
      }},
      "37": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "valueReference": "35"
            }},
            "bandSelectors": {{
              "valueReference": "29"
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "38": {{
        "constantValue": "system:time_start"
      }},
      "39": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "valueReference": "29"
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "40": {{
        "functionInvocationValue": {{
          "arguments": {{
            "dstImg": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "srcImg": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "dstImg": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "dstImg": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "dstImg": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "dstImg": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "dstImg": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "input": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "input": {{
                                                        "argumentReference": "_MAPPING_VAR_0_0"
                                                      }},
                                                      "bandNames": {{
                                                        "arrayValue": {{
                                                          "values": [
                                                            {{
                                                              "valueReference": "21"
                                                            }},
                                                            {{
                                                              "valueReference": "20"
                                                            }}
                                                          ]
                                                        }}
                                                      }}
                                                    }},
                                                    "functionName": "Image.normalizedDifference"
                                                  }}
                                                }},
                                                "names": {{
                                                  "constantValue": [
                                                    "NDVI"
                                                  ]
                                                }}
                                              }},
                                              "functionName": "Image.rename"
                                            }}
                                          }},
                                          "srcImg": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "input": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "input": {{
                                                        "argumentReference": "_MAPPING_VAR_0_0"
                                                      }},
                                                      "bandNames": {{
                                                        "arrayValue": {{
                                                          "values": [
                                                            {{
                                                              "valueReference": "21"
                                                            }},
                                                            {{
                                                              "valueReference": "23"
                                                            }}
                                                          ]
                                                        }}
                                                      }}
                                                    }},
                                                    "functionName": "Image.normalizedDifference"
                                                  }}
                                                }},
                                                "names": {{
                                                  "constantValue": [
                                                    "NBR"
                                                  ]
                                                }}
                                              }},
                                              "functionName": "Image.rename"
                                            }}
                                          }}
                                        }},
                                        "functionName": "Image.addBands"
                                      }}
                                    }},
                                    "srcImg": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "DEFAULT_EXPRESSION_IMAGE": {{
                                                  "argumentReference": "_MAPPING_VAR_0_0"
                                                }},
                                                "B4": {{
                                                  "valueReference": "41"
                                                }},
                                                "B3": {{
                                                  "valueReference": "42"
                                                }},
                                                "B1": {{
                                                  "valueReference": "43"
                                                }}
                                              }},
                                              "functionReference": "44"
                                            }}
                                          }},
                                          "names": {{
                                            "constantValue": [
                                              "EVI"
                                            ]
                                          }}
                                        }},
                                        "functionName": "Image.rename"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Image.addBands"
                                }}
                              }},
                              "srcImg": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "DEFAULT_EXPRESSION_IMAGE": {{
                                            "argumentReference": "_MAPPING_VAR_0_0"
                                          }},
                                          "B4": {{
                                            "valueReference": "41"
                                          }},
                                          "B3": {{
                                            "valueReference": "42"
                                          }}
                                        }},
                                        "functionReference": "50"
                                      }}
                                    }},
                                    "names": {{
                                      "valueReference": "51"
                                    }}
                                  }},
                                  "functionName": "Image.rename"
                                }}
                              }}
                            }},
                            "functionName": "Image.addBands"
                          }}
                        }},
                        "srcImg": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "dstImg": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "dstImg": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "DEFAULT_EXPRESSION_IMAGE": {{
                                                  "argumentReference": "_MAPPING_VAR_0_0"
                                                }},
                                                "L1": {{
                                                  "valueReference": "43"
                                                }},
                                                "B1": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.2043
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L2": {{
                                                  "valueReference": "53"
                                                }},
                                                "B2": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.4158
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L3": {{
                                                  "valueReference": "42"
                                                }},
                                                "B3": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.5524
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L4": {{
                                                  "valueReference": "41"
                                                }},
                                                "B4": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.5741
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L5": {{
                                                  "valueReference": "54"
                                                }},
                                                "B5": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.3124
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L6": {{
                                                  "valueReference": "55"
                                                }},
                                                "B6": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.2303
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }}
                                              }},
                                              "functionReference": "56"
                                            }}
                                          }},
                                          "names": {{
                                            "constantValue": [
                                              "BRIGHTNESS"
                                            ]
                                          }}
                                        }},
                                        "functionName": "Image.rename"
                                      }}
                                    }},
                                    "srcImg": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "DEFAULT_EXPRESSION_IMAGE": {{
                                                  "argumentReference": "_MAPPING_VAR_0_0"
                                                }},
                                                "L1": {{
                                                  "valueReference": "43"
                                                }},
                                                "B1": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": -0.1603
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L2": {{
                                                  "valueReference": "53"
                                                }},
                                                "B2": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": -0.2819
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L3": {{
                                                  "valueReference": "42"
                                                }},
                                                "B3": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": -0.4934
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L4": {{
                                                  "valueReference": "41"
                                                }},
                                                "B4": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": 0.794
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L5": {{
                                                  "valueReference": "54"
                                                }},
                                                "B5": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": -0.0002
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }},
                                                "L6": {{
                                                  "valueReference": "55"
                                                }},
                                                "B6": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "value": {{
                                                        "constantValue": -0.1446
                                                      }}
                                                    }},
                                                    "functionName": "Image.constant"
                                                  }}
                                                }}
                                              }},
                                              "functionReference": "56"
                                            }}
                                          }},
                                          "names": {{
                                            "constantValue": [
                                              "GREENNESS"
                                            ]
                                          }}
                                        }},
                                        "functionName": "Image.rename"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Image.addBands"
                                }}
                              }},
                              "srcImg": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "DEFAULT_EXPRESSION_IMAGE": {{
                                            "argumentReference": "_MAPPING_VAR_0_0"
                                          }},
                                          "L1": {{
                                            "valueReference": "43"
                                          }},
                                          "B1": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": 0.0315
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }},
                                          "L2": {{
                                            "valueReference": "53"
                                          }},
                                          "B2": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": 0.2021
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }},
                                          "L3": {{
                                            "valueReference": "42"
                                          }},
                                          "B3": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": 0.3102
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }},
                                          "L4": {{
                                            "valueReference": "41"
                                          }},
                                          "B4": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": 0.1594
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }},
                                          "L5": {{
                                            "valueReference": "54"
                                          }},
                                          "B5": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": -0.6806
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }},
                                          "L6": {{
                                            "valueReference": "55"
                                          }},
                                          "B6": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "value": {{
                                                  "constantValue": -0.6109
                                                }}
                                              }},
                                              "functionName": "Image.constant"
                                            }}
                                          }}
                                        }},
                                        "functionReference": "56"
                                      }}
                                    }},
                                    "names": {{
                                      "constantValue": [
                                        "WETNESS"
                                      ]
                                    }}
                                  }},
                                  "functionName": "Image.rename"
                                }}
                              }}
                            }},
                            "functionName": "Image.addBands"
                          }}
                        }}
                      }},
                      "functionName": "Image.addBands"
                    }}
                  }},
                  "srcImg": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "input": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "dstImg": {{
                                            "valueReference": "57"
                                          }},
                                          "srcImg": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "input": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "DEFAULT_EXPRESSION_IMAGE": {{
                                                        "valueReference": "58"
                                                      }},
                                                      "GV": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "input": {{
                                                              "valueReference": "58"
                                                            }},
                                                            "bandSelectors": {{
                                                              "arrayValue": {{
                                                                "values": [
                                                                  {{
                                                                    "valueReference": "59"
                                                                  }}
                                                                ]
                                                              }}
                                                            }}
                                                          }},
                                                          "functionName": "Image.select"
                                                        }}
                                                      }},
                                                      "SHADE": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "input": {{
                                                              "valueReference": "58"
                                                            }},
                                                            "bandSelectors": {{
                                                              "arrayValue": {{
                                                                "values": [
                                                                  {{
                                                                    "valueReference": "60"
                                                                  }}
                                                                ]
                                                              }}
                                                            }}
                                                          }},
                                                          "functionName": "Image.select"
                                                        }}
                                                      }},
                                                      "NPV": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "input": {{
                                                              "valueReference": "58"
                                                            }},
                                                            "bandSelectors": {{
                                                              "arrayValue": {{
                                                                "values": [
                                                                  {{
                                                                    "valueReference": "61"
                                                                  }}
                                                                ]
                                                              }}
                                                            }}
                                                          }},
                                                          "functionName": "Image.select"
                                                        }}
                                                      }},
                                                      "SOIL": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "input": {{
                                                              "valueReference": "58"
                                                            }},
                                                            "bandSelectors": {{
                                                              "arrayValue": {{
                                                                "values": [
                                                                  {{
                                                                    "valueReference": "62"
                                                                  }}
                                                                ]
                                                              }}
                                                            }}
                                                          }},
                                                          "functionName": "Image.select"
                                                        }}
                                                      }}
                                                    }},
                                                    "functionReference": "64"
                                                  }}
                                                }},
                                                "names": {{
                                                  "arrayValue": {{
                                                    "values": [
                                                      {{
                                                        "valueReference": "67"
                                                      }}
                                                    ]
                                                  }}
                                                }}
                                              }},
                                              "functionName": "Image.rename"
                                            }}
                                          }}
                                        }},
                                        "functionName": "Image.addBands"
                                      }}
                                    }},
                                    "bandSelectors": {{
                                      "arrayValue": {{
                                        "values": [
                                          {{
                                            "valueReference": "59"
                                          }},
                                          {{
                                            "valueReference": "60"
                                          }},
                                          {{
                                            "valueReference": "61"
                                          }},
                                          {{
                                            "valueReference": "62"
                                          }},
                                          {{
                                            "valueReference": "67"
                                          }}
                                        ]
                                      }}
                                    }}
                                  }},
                                  "functionName": "Image.select"
                                }}
                              }},
                              "names": {{
                                "arrayValue": {{
                                  "values": [
                                    {{
                                      "valueReference": "65"
                                    }},
                                    {{
                                      "constantValue": "Shade"
                                    }},
                                    {{
                                      "valueReference": "66"
                                    }},
                                    {{
                                      "constantValue": "Soil"
                                    }},
                                    {{
                                      "valueReference": "67"
                                    }}
                                  ]
                                }}
                              }}
                            }},
                            "functionName": "Image.rename"
                          }}
                        }},
                        "mask": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "image1": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "valueReference": "57"
                                    }},
                                    "bandSelectors": {{
                                      "arrayValue": {{
                                        "values": [
                                          {{
                                            "valueReference": "63"
                                          }}
                                        ]
                                      }}
                                    }}
                                  }},
                                  "functionName": "Image.select"
                                }}
                              }},
                              "image2": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "value": {{
                                      "constantValue": 0.1
                                    }}
                                  }},
                                  "functionName": "Image.constant"
                                }}
                              }}
                            }},
                            "functionName": "Image.lt"
                          }}
                        }}
                      }},
                      "functionName": "Image.updateMask"
                    }}
                  }}
                }},
                "functionName": "Image.addBands"
              }}
            }}
          }},
          "functionName": "Image.addBands"
        }}
      }},
      "41": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "21"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "42": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "20"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "43": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "18"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "44": {{
        "functionInvocationValue": {{
          "arguments": {{
            "expression": {{
              "constantValue": "float(2.5*(((B4) - (B3)) / ((B4) + (6 * (B3)) - (7.5 * (B1)) + 1)))"
            }},
            "argName": {{
              "valueReference": "45"
            }},
            "vars": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "46"
                  }},
                  {{
                    "valueReference": "47"
                  }},
                  {{
                    "valueReference": "48"
                  }},
                  {{
                    "valueReference": "49"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.parseExpression"
        }}
      }},
      "45": {{
        "valueReference": "46"
      }},
      "46": {{
        "constantValue": "DEFAULT_EXPRESSION_IMAGE"
      }},
      "47": {{
        "constantValue": "B4"
      }},
      "48": {{
        "constantValue": "B3"
      }},
      "49": {{
        "constantValue": "B1"
      }},
      "50": {{
        "functionInvocationValue": {{
          "arguments": {{
            "expression": {{
              "constantValue": "float(2.5*(((B4) - (B3)) / ((B4) + (2.4 * (B3)) + 1)))"
            }},
            "argName": {{
              "valueReference": "45"
            }},
            "vars": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "46"
                  }},
                  {{
                    "valueReference": "47"
                  }},
                  {{
                    "valueReference": "48"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.parseExpression"
        }}
      }},
      "51": {{
        "arrayValue": {{
          "values": [
            {{
              "valueReference": "52"
            }}
          ]
        }}
      }},
      "52": {{
        "constantValue": "EVI2"
      }},
      "53": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "19"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "54": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "22"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "55": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }},
            "bandSelectors": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "23"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.select"
        }}
      }},
      "56": {{
        "functionInvocationValue": {{
          "arguments": {{
            "expression": {{
              "constantValue": "(L1 * B1) + (L2 * B2) + (L3 * B3) + (L4 * B4) + (L5 * B5) + (L6 * B6)"
            }},
            "argName": {{
              "valueReference": "45"
            }},
            "vars": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "46"
                  }},
                  {{
                    "constantValue": "L1"
                  }},
                  {{
                    "valueReference": "49"
                  }},
                  {{
                    "constantValue": "L2"
                  }},
                  {{
                    "constantValue": "B2"
                  }},
                  {{
                    "constantValue": "L3"
                  }},
                  {{
                    "valueReference": "48"
                  }},
                  {{
                    "constantValue": "L4"
                  }},
                  {{
                    "valueReference": "47"
                  }},
                  {{
                    "constantValue": "L5"
                  }},
                  {{
                    "constantValue": "B5"
                  }},
                  {{
                    "constantValue": "L6"
                  }},
                  {{
                    "constantValue": "B6"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.parseExpression"
        }}
      }},
      "57": {{
        "functionInvocationValue": {{
          "arguments": {{
            "dstImg": {{
              "valueReference": "39"
            }},
            "srcImg": {{
              "valueReference": "58"
            }}
          }},
          "functionName": "Image.addBands"
        }}
      }},
      "58": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "image": {{
                    "valueReference": "39"
                  }},
                  "endmembers": {{
                    "constantValue": [
                      [
                        0.05,
                        0.09,
                        0.04,
                        0.61,
                        0.3,
                        0.1
                      ],
                      [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                      ],
                      [
                        0.14,
                        0.17,
                        0.22,
                        0.3,
                        0.55,
                        0.3
                      ],
                      [
                        0.2,
                        0.3,
                        0.34,
                        0.58,
                        0.6,
                        0.58
                      ],
                      [
                        0.9,
                        0.96,
                        0.8,
                        0.78,
                        0.72,
                        0.65
                      ]
                    ]
                  }},
                  "sumToOne": {{
                    "constantValue": true
                  }},
                  "nonNegative": {{
                    "constantValue": true
                  }}
                }},
                "functionName": "Image.unmix"
              }}
            }},
            "names": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "59"
                  }},
                  {{
                    "valueReference": "60"
                  }},
                  {{
                    "valueReference": "61"
                  }},
                  {{
                    "valueReference": "62"
                  }},
                  {{
                    "valueReference": "63"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.rename"
        }}
      }},
      "59": {{
        "constantValue": "band_0"
      }},
      "60": {{
        "constantValue": "band_1"
      }},
      "61": {{
        "constantValue": "band_2"
      }},
      "62": {{
        "constantValue": "band_3"
      }},
      "63": {{
        "constantValue": "band_4"
      }},
      "64": {{
        "functionInvocationValue": {{
          "arguments": {{
            "expression": {{
              "constantValue": "((GV / (1 - SHADE)) - (NPV + SOIL)) / ((GV / (1 - SHADE)) + NPV + SOIL)"
            }},
            "argName": {{
              "valueReference": "45"
            }},
            "vars": {{
              "arrayValue": {{
                "values": [
                  {{
                    "valueReference": "46"
                  }},
                  {{
                    "valueReference": "65"
                  }},
                  {{
                    "constantValue": "SHADE"
                  }},
                  {{
                    "valueReference": "66"
                  }},
                  {{
                    "constantValue": "SOIL"
                  }}
                ]
              }}
            }}
          }},
          "functionName": "Image.parseExpression"
        }}
      }},
      "65": {{
        "constantValue": "GV"
      }},
      "66": {{
        "constantValue": "NPV"
      }},
      "67": {{
        "constantValue": "NDFI"
      }},
      "68": {{
        "constantValue": "year"
      }},
      "69": {{
        "functionInvocationValue": {{
          "arguments": {{
            "date": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "year": {{
                    "valueReference": "70"
                  }},
                  "month": {{
                    "valueReference": "71"
                  }},
                  "day": {{
                    "valueReference": "71"
                  }}
                }},
                "functionName": "Date.fromYMD"
              }}
            }},
            "delta": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "left": {{
                    "argumentReference": "_MAPPING_VAR_0_0"
                  }},
                  "right": {{
                    "valueReference": "70"
                  }}
                }},
                "functionName": "Number.subtract"
              }}
            }},
            "unit": {{
              "valueReference": "68"
            }}
          }},
          "functionName": "Date.advance"
        }}
      }},
      "70": {{
        "functionInvocationValue": {{
          "arguments": {{
            "input": {{
              "argumentReference": "_MAPPING_VAR_0_0"
            }}
          }},
          "functionName": "Number.floor"
        }}
      }},
      "71": {{
        "constantValue": 1
      }},
      "72": {{
        "functionInvocationValue": {{
          "arguments": {{
            "object": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "input": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "image": {{
                          "valueReference": "27"
                        }},
                        "mask": {{
                          "valueReference": "27"
                        }}
                      }},
                      "functionName": "Image.mask"
                    }}
                  }},
                  "names": {{
                    "valueReference": "51"
                  }}
                }},
                "functionName": "Image.rename"
              }}
            }},
            "key": {{
              "valueReference": "38"
            }},
            "value": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "date": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "value": {{
                          "argumentReference": "_MAPPING_VAR_0_0"
                        }}
                      }},
                      "functionName": "Date"
                    }}
                  }}
                }},
                "functionName": "Date.millis"
              }}
            }}
          }},
          "functionName": "Element.set"
        }}
      }},
      "73": {{
        "functionInvocationValue": {{
          "arguments": {{
            "object": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "object": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "object": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "object": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "object": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "object": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "object": {{
                                                  "argumentReference": "_MAPPING_VAR_4_0"
                                                }},
                                                "key": {{
                                                  "valueReference": "74"
                                                }},
                                                "value": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "dictionary": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "image": {{
                                                              "functionInvocationValue": {{
                                                                "arguments": {{
                                                                  "input": {{
                                                                    "argumentReference": "_MAPPING_VAR_4_0"
                                                                  }},
                                                                  "bandSelectors": {{
                                                                    "valueReference": "51"
                                                                  }}
                                                                }},
                                                                "functionName": "Image.select"
                                                              }}
                                                            }},
                                                            "reducer": {{
                                                              "valueReference": "75"
                                                            }},
                                                            "geometry": {{
                                                              "valueReference": "5"
                                                            }},
                                                            "crs": {{
                                                              "valueReference": "76"
                                                            }}
                                                          }},
                                                          "functionName": "Image.reduceRegion"
                                                        }}
                                                      }},
                                                      "key": {{
                                                        "valueReference": "52"
                                                      }}
                                                    }},
                                                    "functionName": "Dictionary.getNumber"
                                                  }}
                                                }}
                                              }},
                                              "functionName": "Element.set"
                                            }}
                                          }},
                                          "key": {{
                                            "constantValue": "fitTime"
                                          }},
                                          "value": {{
                                            "valueReference": "77"
                                          }}
                                        }},
                                        "functionName": "Element.set"
                                      }}
                                    }},
                                    "key": {{
                                      "valueReference": "80"
                                    }},
                                    "value": {{
                                      "valueReference": "81"
                                    }}
                                  }},
                                  "functionName": "Element.set"
                                }}
                              }},
                              "key": {{
                                "constantValue": "coef"
                              }},
                              "value": {{
                                "valueReference": "83"
                              }}
                            }},
                            "functionName": "Element.set"
                          }}
                        }},
                        "key": {{
                          "constantValue": "segment"
                        }},
                        "value": {{
                          "valueReference": "85"
                        }}
                      }},
                      "functionName": "Element.set"
                    }}
                  }},
                  "key": {{
                    "valueReference": "92"
                  }},
                  "value": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "date": {{
                          "valueReference": "79"
                        }},
                        "format": {{
                          "constantValue": "YYYY-MM-dd"
                        }}
                      }},
                      "functionName": "Date.format"
                    }}
                  }}
                }},
                "functionName": "Element.set"
              }}
            }},
            "key": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "number": {{
                    "valueReference": "85"
                  }},
                  "pattern": {{
                    "constantValue": "h%d"
                  }}
                }},
                "functionName": "Number.format"
              }}
            }},
            "value": {{
              "valueReference": "81"
            }}
          }},
          "functionName": "Element.set"
        }}
      }},
      "74": {{
        "constantValue": "value"
      }},
      "75": {{
        "functionInvocationValue": {{
          "arguments": {{}},
          "functionName": "Reducer.first"
        }}
      }},
      "76": {{
        "functionInvocationValue": {{
          "arguments": {{
            "projection": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "crs": {{
                    "constantValue": "EPSG:4326"
                  }}
                }},
                "functionName": "Projection"
              }}
            }},
            "meters": {{
              "constantValue": 30
            }}
          }},
          "functionName": "Projection.atScale"
        }}
      }},
      "77": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "valueReference": "78"
            }},
            "right": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "date": {{
                    "valueReference": "79"
                  }},
                  "start": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "year": {{
                          "valueReference": "78"
                        }},
                        "month": {{
                          "valueReference": "71"
                        }},
                        "day": {{
                          "valueReference": "71"
                        }}
                      }},
                      "functionName": "Date.fromYMD"
                    }}
                  }},
                  "unit": {{
                    "valueReference": "68"
                  }}
                }},
                "functionName": "Date.difference"
              }}
            }}
          }},
          "functionName": "Number.add"
        }}
      }},
      "78": {{
        "functionInvocationValue": {{
          "arguments": {{
            "date": {{
              "valueReference": "79"
            }},
            "unit": {{
              "valueReference": "68"
            }}
          }},
          "functionName": "Date.get"
        }}
      }},
      "79": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image": {{
              "argumentReference": "_MAPPING_VAR_4_0"
            }}
          }},
          "functionName": "Image.date"
        }}
      }},
      "80": {{
        "constantValue": "fit"
      }},
      "81": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "left": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "left": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "left": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "left": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "left": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "left": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "array": {{
                                                        "valueReference": "82"
                                                      }},
                                                      "position": {{
                                                        "constantValue": [
                                                          0
                                                        ]
                                                      }}
                                                    }},
                                                    "functionName": "Array.get"
                                                  }}
                                                }},
                                                "right": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "left": {{
                                                        "functionInvocationValue": {{
                                                          "arguments": {{
                                                            "array": {{
                                                              "valueReference": "82"
                                                            }},
                                                            "position": {{
                                                              "valueReference": "88"
                                                            }}
                                                          }},
                                                          "functionName": "Array.get"
                                                        }}
                                                      }},
                                                      "right": {{
                                                        "valueReference": "77"
                                                      }}
                                                    }},
                                                    "functionName": "Number.multiply"
                                                  }}
                                                }}
                                              }},
                                              "functionName": "Number.add"
                                            }}
                                          }},
                                          "right": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "left": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "array": {{
                                                        "valueReference": "82"
                                                      }},
                                                      "position": {{
                                                        "constantValue": [
                                                          2
                                                        ]
                                                      }}
                                                    }},
                                                    "functionName": "Array.get"
                                                  }}
                                                }},
                                                "right": {{
                                                  "functionInvocationValue": {{
                                                    "arguments": {{
                                                      "input": {{
                                                        "valueReference": "89"
                                                      }}
                                                    }},
                                                    "functionName": "Number.cos"
                                                  }}
                                                }}
                                              }},
                                              "functionName": "Number.multiply"
                                            }}
                                          }}
                                        }},
                                        "functionName": "Number.add"
                                      }}
                                    }},
                                    "right": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "left": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "array": {{
                                                  "valueReference": "82"
                                                }},
                                                "position": {{
                                                  "constantValue": [
                                                    3
                                                  ]
                                                }}
                                              }},
                                              "functionName": "Array.get"
                                            }}
                                          }},
                                          "right": {{
                                            "functionInvocationValue": {{
                                              "arguments": {{
                                                "input": {{
                                                  "valueReference": "89"
                                                }}
                                              }},
                                              "functionName": "Number.sin"
                                            }}
                                          }}
                                        }},
                                        "functionName": "Number.multiply"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Number.add"
                                }}
                              }},
                              "right": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "left": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "array": {{
                                            "valueReference": "82"
                                          }},
                                          "position": {{
                                            "constantValue": [
                                              4
                                            ]
                                          }}
                                        }},
                                        "functionName": "Array.get"
                                      }}
                                    }},
                                    "right": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "input": {{
                                            "valueReference": "90"
                                          }}
                                        }},
                                        "functionName": "Number.cos"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Number.multiply"
                                }}
                              }}
                            }},
                            "functionName": "Number.add"
                          }}
                        }},
                        "right": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "left": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "array": {{
                                      "valueReference": "82"
                                    }},
                                    "position": {{
                                      "constantValue": [
                                        5
                                      ]
                                    }}
                                  }},
                                  "functionName": "Array.get"
                                }}
                              }},
                              "right": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "input": {{
                                      "valueReference": "90"
                                    }}
                                  }},
                                  "functionName": "Number.sin"
                                }}
                              }}
                            }},
                            "functionName": "Number.multiply"
                          }}
                        }}
                      }},
                      "functionName": "Number.add"
                    }}
                  }},
                  "right": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "left": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "array": {{
                                "valueReference": "82"
                              }},
                              "position": {{
                                "constantValue": [
                                  6
                                ]
                              }}
                            }},
                            "functionName": "Array.get"
                          }}
                        }},
                        "right": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "input": {{
                                "valueReference": "91"
                              }}
                            }},
                            "functionName": "Number.cos"
                          }}
                        }}
                      }},
                      "functionName": "Number.multiply"
                    }}
                  }}
                }},
                "functionName": "Number.add"
              }}
            }},
            "right": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "left": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "array": {{
                          "valueReference": "82"
                        }},
                        "position": {{
                          "constantValue": [
                            7
                          ]
                        }}
                      }},
                      "functionName": "Array.get"
                    }}
                  }},
                  "right": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "input": {{
                          "valueReference": "91"
                        }}
                      }},
                      "functionName": "Number.sin"
                    }}
                  }}
                }},
                "functionName": "Number.multiply"
              }}
            }}
          }},
          "functionName": "Number.add"
        }}
      }},
      "82": {{
        "functionInvocationValue": {{
          "arguments": {{
            "values": {{
              "valueReference": "83"
            }}
          }},
          "functionName": "Array"
        }}
      }},
      "83": {{
        "functionInvocationValue": {{
          "arguments": {{
            "condition": {{
              "valueReference": "84"
            }},
            "trueCase": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "array": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "array": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "dictionary": {{
                                "valueReference": "86"
                              }},
                              "key": {{
                                "constantValue": "EVI2_coefs"
                              }}
                            }},
                            "functionName": "Dictionary.getArray"
                          }}
                        }},
                        "axis": {{
                          "constantValue": 0
                        }},
                        "start": {{
                          "valueReference": "85"
                        }},
                        "end": {{
                          "valueReference": "84"
                        }}
                      }},
                      "functionName": "Array.slice"
                    }}
                  }},
                  "axes": {{
                    "valueReference": "88"
                  }}
                }},
                "functionName": "Array.project"
              }}
            }},
            "falseCase": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "values": {{
                    "constantValue": [
                      0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0,
                      0
                    ]
                  }}
                }},
                "functionName": "Array"
              }}
            }}
          }},
          "functionName": "If"
        }}
      }},
      "84": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "valueReference": "85"
            }},
            "right": {{
              "valueReference": "71"
            }}
          }},
          "functionName": "Number.add"
        }}
      }},
      "85": {{
        "functionInvocationValue": {{
          "arguments": {{
            "list": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "array": {{
                    "functionInvocationValue": {{
                      "arguments": {{
                        "left": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "left": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "values": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "dictionary": {{
                                            "valueReference": "86"
                                          }},
                                          "key": {{
                                            "constantValue": "tStart"
                                          }}
                                        }},
                                        "functionName": "Dictionary.get"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Array"
                                }}
                              }},
                              "right": {{
                                "valueReference": "87"
                              }}
                            }},
                            "functionName": "Array.lte"
                          }}
                        }},
                        "right": {{
                          "functionInvocationValue": {{
                            "arguments": {{
                              "left": {{
                                "functionInvocationValue": {{
                                  "arguments": {{
                                    "values": {{
                                      "functionInvocationValue": {{
                                        "arguments": {{
                                          "dictionary": {{
                                            "valueReference": "86"
                                          }},
                                          "key": {{
                                            "constantValue": "tEnd"
                                          }}
                                        }},
                                        "functionName": "Dictionary.get"
                                      }}
                                    }}
                                  }},
                                  "functionName": "Array"
                                }}
                              }},
                              "right": {{
                                "valueReference": "87"
                              }}
                            }},
                            "functionName": "Array.gte"
                          }}
                        }}
                      }},
                      "functionName": "Array.and"
                    }}
                  }}
                }},
                "functionName": "Array.toList"
              }}
            }},
            "element": {{
              "constantValue": 1
            }}
          }},
          "functionName": "List.indexOf"
        }}
      }},
      "86": {{
        "functionInvocationValue": {{
          "arguments": {{
            "image": {{
              "functionInvocationValue": {{
                "arguments": {{
                  "collection": {{
                    "valueReference": "2"
                  }},
                  "breakpointBands": {{
                    "arrayValue": {{
                      "values": [
                        {{
                          "valueReference": "19"
                        }},
                        {{
                          "valueReference": "20"
                        }},
                        {{
                          "valueReference": "21"
                        }},
                        {{
                          "valueReference": "22"
                        }},
                        {{
                          "valueReference": "23"
                        }}
                      ]
                    }}
                  }},
                  "tmaskBands": {{
                    "arrayValue": {{
                      "values": [
                        {{
                          "valueReference": "19"
                        }},
                        {{
                          "valueReference": "23"
                        }}
                      ]
                    }}
                  }},
                  "minObservations": {{
                    "constantValue": 6
                  }},
                  "chiSquareProbability": {{
                    "constantValue": 0.99
                  }},
                  "minNumOfYearsScaler": {{
                    "constantValue": 1.33
                  }},
                  "dateFormat": {{
                    "valueReference": "71"
                  }},
                  "lambda": {{
                    "constantValue": 0.002
                  }},
                  "maxIterations": {{
                    "constantValue": 10000
                  }}
                }},
                "functionName": "TemporalSegmentation.Ccdc"
              }}
            }},
            "reducer": {{
              "valueReference": "75"
            }},
            "geometry": {{
              "valueReference": "5"
            }},
            "crs": {{
              "valueReference": "76"
            }}
          }},
          "functionName": "Image.reduceRegion"
        }}
      }},
      "87": {{
        "functionInvocationValue": {{
          "arguments": {{
            "values": {{
              "valueReference": "77"
            }}
          }},
          "functionName": "Array"
        }}
      }},
      "88": {{
        "constantValue": [
          1
        ]
      }},
      "89": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "valueReference": "77"
            }},
            "right": {{
              "constantValue": 6.283185307179586
            }}
          }},
          "functionName": "Number.multiply"
        }}
      }},
      "90": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "valueReference": "77"
            }},
            "right": {{
              "constantValue": 12.566370614359172
            }}
          }},
          "functionName": "Number.multiply"
        }}
      }},
      "91": {{
        "functionInvocationValue": {{
          "arguments": {{
            "left": {{
              "valueReference": "77"
            }},
            "right": {{
              "constantValue": 18.84955592153876
            }}
          }},
          "functionName": "Number.multiply"
        }}
      }},
      "92": {{
        "constantValue": "dateString"
      }},
      "93": {{
        "constantValue": 9
      }}
    }}
  }}
}}"""
    return body 
